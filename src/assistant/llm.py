from __future__ import annotations
import requests


class OllamaClient:
    def __init__(self, base_url: str, model: str, timeout: int = 60):
        self.url = base_url.rstrip("/") + "/api/generate"
        self.model = model
        self.timeout = timeout

    def generate(self, prompt: str) -> str:
        response = requests.post(
            self.url,
            json={"model": self.model, "prompt": prompt, "stream": False},
            timeout=self.timeout,
        )
        response.raise_for_status()
        payload = response.json()
        text = payload.get("response")
        if not text:
            raise ValueError("Ollama retornou uma resposta vazia.")
        return text.strip()
