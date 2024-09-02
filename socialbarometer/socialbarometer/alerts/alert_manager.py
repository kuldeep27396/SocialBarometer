from socialbarometer.socialbarometer.utils.logger import setup_logger


class AlertManager:
    def __init__(self, db_manager, threshold):
        self.db_manager = db_manager
        self.threshold = threshold
        self.logger = setup_logger("AlertManager")

    async def check_and_send_alerts(self, item, sentiment):
        if abs(sentiment[1]) > self.threshold:
            await self.send_alert(item, sentiment)

    async def send_alert(self, item, sentiment):
        self.logger.info(f"ALERT: {sentiment[0].upper()} sentiment detected!")
        self.logger.info(f"Text: {item['text']}")
        self.logger.info(f"Platform: {item['platform']}")
        self.logger.info(f"Sentiment score: {sentiment[1]}")

        # Save the alert to the database
        await self.db_manager.save_alert(item, sentiment)