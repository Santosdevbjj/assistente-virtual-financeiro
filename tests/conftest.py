import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from assistant.config import settings
from assistant.knowledge import KnowledgeBase
from assistant.service import FinancialAssistant


@pytest.fixture
def knowledge():
    return KnowledgeBase(settings.data_dir)


@pytest.fixture
def assistant(knowledge):
    return FinancialAssistant(knowledge)
