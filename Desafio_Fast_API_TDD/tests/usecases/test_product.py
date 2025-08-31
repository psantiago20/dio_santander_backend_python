from typing import List
from uuid import UUID
import pytest
from store.core.exceptions import NotFoundException
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import ProductUsecase


@pytest.mark.asyncio
async def test_usecases_create_should_return_success(mongo_client, product_in):
    usecase = ProductUsecase(mongo_client)

    result = await usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


@pytest.mark.asyncio
async def test_usecases_get_should_return_success(
    mongo_client, product_in, product_inserted
):
    usecase = ProductUsecase(mongo_client)

    await usecase.create(body=product_in)

    result = await usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


@pytest.mark.asyncio
async def test_usecases_get_should_not_success(mongo_client, product_in, product_id):
    usecase = ProductUsecase(mongo_client)

    await usecase.create(body=product_in)

    with pytest.raises(NotFoundException) as err:
        await usecase.get(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_should_return_success(mongo_client, product_in):
    usecase = ProductUsecase(mongo_client)

    await usecase.create(body=product_in)

    result = await usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1


@pytest.mark.asyncio
async def test_usecases_update_should_return_success(
    mongo_client, product_in, product_up, product_inserted
):
    usecase = ProductUsecase(mongo_client)

    await usecase.create(body=product_in)

    product_up.price = "7.500"

    result = await usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


@pytest.mark.asyncio
async def test_usecases_delete_should_return_success(
    mongo_client, product_in, product_inserted
):
    usecase = ProductUsecase(mongo_client)

    await usecase.create(body=product_in)

    result = await usecase.delete(id=product_inserted.id)

    assert result is True


@pytest.mark.asyncio
async def test_usecases_delete_should_not_found(mongo_client, product_in):
    usecase = ProductUsecase(mongo_client)

    await usecase.create(body=product_in)

    with pytest.raises(NotFoundException) as err:
        await usecase.delete(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )
