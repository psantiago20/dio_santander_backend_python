import asyncio
import pytest
from store.schemas.product import ProductIn, ProductUpdate
from store.usecases.product import ProductUsecase
from tests.factories import product_data, products_data
from uuid import UUID
from httpx import ASGITransport, AsyncClient
from store.db.mongo import db_client


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop


@pytest.fixture
async def mongo_client():
    client = db_client.get()
    yield client
    await db_client.close()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    collections_names = await mongo_client.get_database().list_collection_names()
    for collection_name in collections_names:
        if not collection_name.startswith("system"):
            await mongo_client.get_database()[collection_name].delete_many({})


@pytest.fixture
def product_usecase(mongo_client):
    return ProductUsecase(mongo_client)


@pytest.fixture
async def client():
    from store.main import app

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def products_url() -> str:
    return "/products/"


@pytest.fixture
def product_id() -> UUID:
    return UUID("fce6cc37-10b9-4a8e-a8b2-977df327001a")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_data(), id=product_id)


@pytest.fixture
def product_up(product_id):
    return ProductUpdate(**product_data(), id=product_id)


@pytest.fixture
async def product_inserted(product_usecase, product_in):
    return await product_usecase.create(body=product_in)


@pytest.fixture
def products_in():
    return [ProductIn(**product) for product in products_data()]


@pytest.fixture
async def products_inserted(product_usecase, products_in):
    return [await product_usecase.create(body=product_in) for product_in in products_in]
