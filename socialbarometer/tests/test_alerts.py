import pytest
from socialbarometer.alerts.alert_manager import AlertManager
from socialbarometer.database.db_manager import DBManager


class MockDBManager:
    async def save_alert(self, item, sentiment):
        pass


@pytest.mark.asyncio
async def test_alert_manager():
    db_manager = MockDBManager()
    alert_manager = AlertManager(db_manager, threshold=0.5)

    item = {
        'text': 'Test text',
        'user': 'testuser',
        'timestamp': '2023-01-01T00:00:00',
        'platform': 'test'
    }

    # Test with sentiment above threshold
    await alert_manager.check_and_send_alerts(item, ('positive', 0.8))

    # Test with sentiment below threshold
    await alert_manager.check_and_send_alerts(item, ('neutral', 0.2))