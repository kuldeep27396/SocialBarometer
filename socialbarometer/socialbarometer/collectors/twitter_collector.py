import tweepy
from .base_collector import BaseCollector

class TwitterCollector(BaseCollector):
    def __init__(self, api_key, api_secret):
        super().__init__("TwitterCollector")
        auth = tweepy.AppAuthHandler(api_key, api_secret)
        self.api = tweepy.API(auth)

    async def collect(self, keywords):
        try:
            tweets = self.api.search_tweets(q=keywords, count=100)
            return [
                {
                    'text': tweet.text,
                    'user': tweet.user.screen_name,
                    'timestamp': tweet.created_at,
                    'platform': 'twitter'
                }
                for tweet in tweets
            ]
        except tweepy.TooManyRequests:
            await self.handle_rate_limit()
            return []