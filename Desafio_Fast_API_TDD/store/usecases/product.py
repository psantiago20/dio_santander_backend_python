from typing import List, Optional, Dict, Any
from uuid import UUID
from decimal import Decimal
from datetime import datetime, timezone

from bson import Decimal128
import pymongo
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from store.db.mongo import db_client
from store.models.product import ProductModel
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from store.core.exceptions import NotFoundException


def _to_mongo_set(doc: Dict[str, Any]) -> Dict[str, Any]:
    """
    Converte campos Python -> tipos BSON apropriados para update.
    - price -> Decimal128
    - ignora None (já devem estar filtrados no exclude_none)
    """
    out: Dict[str, Any] = {}

    for k, v in doc.items():
        if v is None:
            continue
        if k == "price":
            # aceita Decimal, str, etc. -> força Decimal128
            out[k] = Decimal128(str(v))
        else:
            out[k] = v
    return out


class ProductUsecase:
    def __init__(self, client: AsyncIOMotorClient | None = None) -> None:
        self.client: AsyncIOMotorClient = client or db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product_model = ProductModel(**body.model_dump())
        # ProductModel.model_dump() já converte Decimal -> Decimal128 via model_serializer do CreateBaseModel
        await self.collection.insert_one(product_model.model_dump())
        return ProductOut(**product_model.model_dump())

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})
        if not result:
            raise NotFoundException(message=f"Product not found with filter: {id}")
        return ProductOut(**result)

    async def query(
        self,
        min_price: Optional[Decimal] = None,
        max_price: Optional[Decimal] = None,
    ) -> List[ProductOut]:
        mongo_filter: Dict[str, Any] = {}

        if min_price is not None or max_price is not None:
            price_cond: Dict[str, Any] = {}
            if min_price is not None:
                price_cond["$gt"] = Decimal128(str(min_price))
            if max_price is not None:
                price_cond["$lt"] = Decimal128(str(max_price))
            mongo_filter["price"] = price_cond

        return [ProductOut(**item) async for item in self.collection.find(mongo_filter)]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        # pega só campos enviados e não-nulos
        payload = body.model_dump(exclude_unset=True, exclude_none=True)

        # updated_at: se não vier no body, atualiza com now()
        if "updated_at" not in payload:
            payload["updated_at"] = datetime.now(timezone.utc)

        # converte para tipos BSON apropriados (ex: Decimal128)
        set_doc = _to_mongo_set(payload)

        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": set_doc},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        if result is None:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        # Retorna o documento atualizado; ProductUpdateOut deve aceitar os campos retornados
        return ProductUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": id})
        if not product:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        result = await self.collection.delete_one({"id": id})
        return result.deleted_count > 0
