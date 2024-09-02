import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
    REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
    ALERT_THRESHOLD = float(os.getenv("ALERT_THRESHOLD", "0.7"))
    COLLECTION_INTERVAL = int(os.getenv("COLLECTION_INTERVAL", "300"))
    SEARCH_KEYWORDS = os.getenv("SEARCH_KEYWORDS", "SocialBarometer,sentiment analysis")