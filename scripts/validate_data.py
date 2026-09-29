from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from assistant.config import settings
from assistant.knowledge import KnowledgeBase

if __name__ == "__main__":
    kb = KnowledgeBase(settings.data_dir)
    print("OK: base carregada")
    print(f"Perfil: {kb.profile.nome}")
    print(f"Transações: {len(kb.transactions)}")
    print(f"Atendimentos: {len(kb.history)}")
    print(f"Produtos: {len(kb.products)}")
