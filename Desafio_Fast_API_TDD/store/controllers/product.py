from typing import List, Optional
from decimal import Decimal
from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query, status
from pydantic import UUID4
from pymongo.errors import PyMongoError

from store.core.exceptions import NotFoundException
from store.schemas.product import ProductIn, ProductOut, ProductUpdate
from store.usecases.product import ProductUsecase

router = APIRouter(tags=["products"])


def get_product_usecase() -> ProductUsecase:
    return ProductUsecase()


@router.post(path="/", status_code=status.HTTP_201_CREATED, response_model=ProductOut)
async def post(
    body: ProductIn = Body(...),
    usecase: ProductUsecase = Depends(get_product_usecase),
) -> ProductOut:
    try:
        return await usecase.create(body=body)
    except PyMongoError:
        # Mapeia erro de inserção para resposta amigável
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Falha ao inserir o produto.",
        )
    except Exception:
        # fallback (caso outro erro ocorra)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro inesperado ao criar o produto.",
        )


@router.get(path="/{id}", status_code=status.HTTP_200_OK, response_model=ProductOut)
async def get(
    id: UUID4 = Path(...),
    usecase: ProductUsecase = Depends(get_product_usecase),
) -> ProductOut:
    try:
        return await usecase.get(id=id)
    except NotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        )


@router.get(path="/", status_code=status.HTTP_200_OK, response_model=List[ProductOut])
async def query(
    min_price: Optional[Decimal] = Query(default=None),
    max_price: Optional[Decimal] = Query(default=None),
    usecase: ProductUsecase = Depends(get_product_usecase),
) -> List[ProductOut]:
    return await usecase.query(min_price=min_price, max_price=max_price)


@router.patch(path="/{id}", status_code=status.HTTP_200_OK, response_model=ProductOut)
async def patch(
    id: UUID4 = Path(...),
    body: ProductUpdate = Body(...),
    usecase: ProductUsecase = Depends(get_product_usecase),
) -> ProductOut:
    try:
        return await usecase.update(id=id, body=body)
    except NotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        )
    except PyMongoError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Falha ao atualizar o produto.",
        )


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: UUID4 = Path(...),
    usecase: ProductUsecase = Depends(get_product_usecase),
) -> None:
    try:
        await usecase.delete(id=id)
    except NotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message,
        )
