import asyncio
from socialbarometer.socialbarometer.collectors.twitter_collector import TwitterCollector
from socialbarometer.socialbarometer.collectors.reddit_collector import RedditCollector
from socialbarometer.socialbarometer.analyzers.sentiment_analyzer import SentimentAnalyzer
from socialbarometer.socialbarometer.alerts.alert_manager import AlertManager
from socialbarometer.socialbarometer.database.db_manager import DBManager
from socialbarometer.socialbarometer.utils.config import Config
from socialbarometer.socialbarometer.utils.logger import setup_logger

logger = setup_logger(__name__)


async def main():
    config = Config()
    db_manager = DBManager(config.DATABASE_URL)
    alert_manager = AlertManager(db_manager, config.ALERT_THRESHOLD)
    sentiment_analyzer = SentimentAnalyzer()

    collectors = [
        TwitterCollector(config.TWITTER_API_KEY, config.TWITTER_API_SECRET),
        RedditCollector(config.REDDIT_CLIENT_ID, config.REDDIT_CLIENT_SECRET)
    ]

    while True:
        for collector in collectors:
            try:
                data = await collector.collect(config.SEARCH_KEYWORDS)
                for item in data:
                    sentiment = sentiment_analyzer.analyze(item['text'])
                    await db_manager.save_item(item, sentiment)
                    await alert_manager.check_and_send_alerts(item, sentiment)
            except Exception as e:
                logger.error(f"Error in collection: {str(e)}")

        await asyncio.sleep(config.COLLECTION_INTERVAL)


if __name__ == "__main__":
    asyncio.run(main())

# To run the project:
# 
# Install dependencies: poetry install
# Set up your .env file with the necessary credentials and configuration
# Run the main script: poetry run python -m socialbarometer.socialbarometer.socialbarometer.socialbarometer.main
# 
# To run tests: poetry run pytest