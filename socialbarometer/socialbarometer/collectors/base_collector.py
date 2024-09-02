from abc import ABC, abstractmethod
from socialbarometer.socialbarometer.utils.logger import setup_logger

class BaseCollector(ABC):
    def __init__(self, name):
        self.logger = setup_logger(name)

    @abstractmethod
    async def collect(self, keywords):
        pass

    async def handle_rate_limit(self):
        self.logger.warning("Rate limit reached. Implementing backoff strategy.")
        # Implement backoff strategy here