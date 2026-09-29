from __future__ import annotations
import re
from .schemas import GuardrailResult

OFF_TOPIC_PATTERNS = [
    r"\bprevis[aã]o do tempo\b", r"\bclima\b", r"\breceita de bolo\b",
    r"\bfutebol\b", r"\bfilme\b",
]
SENSITIVE_PATTERNS = [
    r"\bsenha\b", r"\bpassword\b", r"\btoken\b",
    r"\bcart[aã]o\b.*\b\d{4,}\b", r"\bcpf\b.*\b\d\b", r"\bapi[_ -]?key\b",
]
RECOMMENDATION_PATTERNS = [
    r"\bdevo investir\b", r"\bonde devo investir\b",
    r"\bqual investimento comprar\b", r"\bqual a melhor a[cç][aã]o\b",
    r"\bme diga onde investir\b", r"\brecomende\b.*\binvest",
]


def classify_message(message: str) -> GuardrailResult:
    text = message.casefold().strip()
    if any(re.search(pattern, text) for pattern in SENSITIVE_PATTERNS):
        return GuardrailResult(allowed=False, category="sensitive",
                               reason="Solicitação de informação potencialmente sensível.")
    if any(re.search(pattern, text) for pattern in RECOMMENDATION_PATTERNS):
        return GuardrailResult(allowed=False, category="recommendation",
                               reason="O agente é educacional e não fornece recomendação personalizada.")
    if any(re.search(pattern, text) for pattern in OFF_TOPIC_PATTERNS):
        return GuardrailResult(allowed=False, category="off_topic",
                               reason="A solicitação está fora do escopo financeiro.")
    return GuardrailResult(allowed=True, category="allowed")


def safe_fallback(result: GuardrailResult) -> str:
    messages = {
        "sensitive": "Não posso acessar ou compartilhar senhas, credenciais, tokens ou dados sensíveis. Posso ajudar com informações financeiras fictícias da base de demonstração.",
        "recommendation": "Este assistente é educativo e não recomenda investimentos específicos. Posso explicar conceitos, riscos e características dos produtos existentes na base.",
        "off_topic": "Sou um assistente voltado à educação financeira e não tenho informação confiável para esse assunto. Posso ajudar com gastos, metas e conceitos financeiros.",
    }
    return messages.get(result.category, "Não consigo atender a essa solicitação dentro do escopo deste protótipo.")
