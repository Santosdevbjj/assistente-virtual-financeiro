from dataclasses import dataclass
import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")


@dataclass(frozen=True)
class Settings:
    data_dir: Path = ROOT_DIR / "data"
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "gpt-oss")
    llm_enabled: bool = os.getenv("LLM_ENABLED", "false").lower() == "true"
    request_timeout_seconds: int = int(os.getenv("OLLAMA_TIMEOUT_SECONDS", "60"))


settings = Settings()
