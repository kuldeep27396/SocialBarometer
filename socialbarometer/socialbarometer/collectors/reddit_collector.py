import praw
from .base_collector import BaseCollector

class RedditCollector(BaseCollector):
    def __init__(self, client_id, client_secret):
        super().__init__("RedditCollector")
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent="SocialBarometer 1.0"
        )

    async def collect(self, keywords):
        try:
            subreddit = self.reddit.subreddit("all")
            posts = subreddit.search(keywords, limit=100, sort="new")
            return [
                {
                    'text': post.title + " " + post.selftext,
                    'user': post.author.name if post.author else "[deleted]",
                    'timestamp': post.created_utc,
                    'platform': 'reddit'
                }
                for post in posts
            ]
        except Exception as e:
            self.logger.error(f"Error collecting Reddit data: {str(e)}")
            return []