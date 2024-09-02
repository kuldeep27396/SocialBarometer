import pytest
from socialbarometer.collectors.twitter_collector import TwitterCollector
from socialbarometer.collectors.reddit_collector import RedditCollector

@pytest.mark.asyncio
async def test_twitter_collector():
    collector = TwitterCollector("dummy_key", "dummy_secret")
    results = await collector.collect("test")
    assert isinstance(results, list)
    if results:
        assert all(key in results[0] for key in ['text', 'user', 'timestamp', 'platform'])

@pytest.mark.asyncio
async def test_reddit_collector():
    collector = RedditCollector("dummy_id", "dummy_secret")
    results = await collector.collect("test")
    assert isinstance(results, list)
    if results:
        assert all(key in results[0] for key in ['text', 'user', 'timestamp', 'platform'])