import pytest
from unittest.mock import MagicMock
from core.scraper import FacebookScraper

@pytest.fixture
def mock_db():
    return MagicMock()

def test_save_results(mock_db):
    scraper = FacebookScraper()
    scraper.db = mock_db
    scraper.save_results([])
    mock_db.Session.assert_called_once()  # Verifica interacciones [[5]]