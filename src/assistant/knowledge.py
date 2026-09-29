from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from .schemas import Product, Profile


class KnowledgeBase:
    """Carrega e normaliza os quatro artefatos mockados do desafio."""

    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.profile = self._load_profile()
        self.transactions = self._load_transactions()
        self.history = self._load_history()
        self.products = self._load_products()

    def _load_profile(self) -> Profile:
        with (self.data_dir / "perfil_investidor.json").open(encoding="utf-8") as fp:
            return Profile.model_validate(json.load(fp))

    def _load_transactions(self) -> pd.DataFrame:
        df = pd.read_csv(self.data_dir / "transacoes.csv")
        required = {"data", "descricao", "categoria", "valor", "tipo"}
        missing = required - set(df.columns)
        if missing:
            raise ValueError(f"Colunas ausentes em transacoes.csv: {sorted(missing)}")
        df["data"] = pd.to_datetime(df["data"], errors="raise")
        df["valor"] = pd.to_numeric(df["valor"], errors="raise")
        df["tipo"] = df["tipo"].str.lower().str.strip()
        return df

    def _load_history(self) -> pd.DataFrame:
        df = pd.read_csv(self.data_dir / "historico_atendimento.csv")
        df["data"] = pd.to_datetime(df["data"], errors="raise")
        return df

    def _load_products(self) -> list[Product]:
        with (self.data_dir / "produtos_financeiros.json").open(encoding="utf-8") as fp:
            return [Product.model_validate(item) for item in json.load(fp)]

    def product_by_name(self, name: str) -> Product | None:
        normalized = name.casefold()
        return next((p for p in self.products if p.nome.casefold() == normalized), None)

    def snapshot(self) -> dict:
        return {
            "profile": self.profile.model_dump(),
            "transactions": self.transactions.to_dict(orient="records"),
            "history": self.history.to_dict(orient="records"),
            "products": [p.model_dump() for p in self.products],
        }
