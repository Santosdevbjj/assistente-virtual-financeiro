from typing import Literal
from pydantic import BaseModel, Field


class Profile(BaseModel):
    nome: str
    idade: int
    profissao: str
    renda_mensal: float = Field(ge=0)
    perfil_investidor: str
    objetivo_principal: str
    patrimonio_total: float = Field(ge=0)
    reserva_emergencia_atual: float = Field(ge=0)
    aceita_risco: bool
    metas: list[dict]


class Product(BaseModel):
    nome: str
    categoria: str
    risco: str
    rentabilidade: str
    aporte_minimo: float = Field(ge=0)
    indicado_para: str


class GuardrailResult(BaseModel):
    allowed: bool
    reason: str | None = None
    category: Literal["allowed", "off_topic", "sensitive", "recommendation", "unknown"] = "allowed"
