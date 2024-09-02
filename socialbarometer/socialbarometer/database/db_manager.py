import asyncpg
from socialbarometer.socialbarometer.utils.logger import setup_logger

class DBManager:
    def __init__(self, db_url):
        self.db_url = db_url
        self.logger = setup_logger("DBManager")

    async def get_connection(self):
        return await asyncpg.connect(self.db_url)

    async def save_item(self, item, sentiment):
        query = """
        INSERT INTO social_media_items (text, user, timestamp, platform, sentiment, sentiment_score)
        VALUES ($1, $2, $3, $4, $5, $6)
        """
        async with await self.get_connection() as conn:
            await conn.execute(query, item['text'], item['user'], item['timestamp'],
                               item['platform'], sentiment[0], sentiment[1])

    async def save_alert(self, item, sentiment):
        query = """
        INSERT INTO alerts (text, user, timestamp, platform, sentiment, sentiment_score)
        VALUES ($1, $2, $3, $4, $5, $6)
        """
        async with await self.get_connection() as conn:
            await conn.execute(query, item['text'], item['user'], item['timestamp'],
                               item['platform'], sentiment[0], sentiment[1])