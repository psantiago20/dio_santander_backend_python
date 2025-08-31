from bson import Decimal128
from store.models.base import CreateBaseModel
from store.schemas.product import ProductIn


class ProductModel(ProductIn, CreateBaseModel):
    def to_mongo(self) -> dict:
        """
        Retorna o dicionário pronto para salvar no MongoDB,
        convertendo Decimals em Decimal128.
        """
        data = self.model_dump()
        for key, value in data.items():
            if isinstance(value, float) or isinstance(value, str):
                # se vier em string/float, mantém como está
                continue
            if hasattr(value, "as_tuple"):  # é um Decimal
                data[key] = Decimal128(str(value))
        return data
