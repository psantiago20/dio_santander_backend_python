from motor.motor_asyncio import AsyncIOMotorClient
from store.core.config import settings


class MongoClient:
    def __init__(self, uri: str = settings.DATABASE_URL):
        self._uri = uri
        self._client: AsyncIOMotorClient | None = None

    def get(self) -> AsyncIOMotorClient:
        if not self._client:
            self._client = AsyncIOMotorClient(self._uri)
        return self._client

    async def close(self):
        if self._client:
            self._client.close()
            self._client = None


db_client = MongoClient()
