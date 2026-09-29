from pathlib import Path
import sys

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assistant.config import settings
from assistant.knowledge import KnowledgeBase
from assistant.llm import OllamaClient
from assistant.service import FinancialAssistant
from assistant.analytics import financial_summary

st.set_page_config(page_title="Nexo — Assistente Financeiro", page_icon="🤖", layout="wide")


@st.cache_resource
def load_assistant():
    kb = KnowledgeBase(settings.data_dir)
    llm = None
    if settings.llm_enabled:
        llm = OllamaClient(
            settings.ollama_base_url,
            settings.ollama_model,
            settings.request_timeout_seconds,
        )
    return FinancialAssistant(kb, llm), kb


assistant, kb = load_assistant()
summary = financial_summary(kb.transactions, kb.profile)

st.title("🤖 Nexo — Assistente Virtual Financeiro")
st.caption("Educação financeira contextualizada • Dados fictícios • Sem recomendação de investimentos")

with st.sidebar:
    st.header("Contexto da demonstração")
    st.write(f"**Cliente:** {kb.profile.nome}")
    st.write(f"**Perfil informado:** {kb.profile.perfil_investidor}")
    st.write(f"**Objetivo:** {kb.profile.objetivo_principal}")
    st.divider()
    st.metric("Receitas", f"R$ {summary['receitas']:,.2f}")
    st.metric("Despesas", f"R$ {summary['despesas']:,.2f}")
    st.metric("Saldo do período", f"R$ {summary['saldo_periodo']:,.2f}")
    st.caption("Valores provenientes exclusivamente do dataset fictício.")

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Reserva atual", f"R$ {kb.profile.reserva_emergencia_atual:,.2f}")
with c2:
    st.metric("Lacuna da reserva", f"R$ {summary['lacuna_reserva']:,.2f}")
with c3:
    st.metric("Categorias de saída", len(summary["despesas_por_categoria"]))

st.subheader("Converse com o assistente")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ex.: Quanto gastei com alimentação?")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    answer = assistant.answer(prompt)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)

st.divider()
st.subheader("Exemplos para testar")
examples = [
    "Quanto gastei com alimentação?",
    "Onde estou gastando mais?",
    "Qual é o meu saldo no período?",
    "Como está minha reserva de emergência?",
    "O que é o CDB Liquidez Diária?",
    "Devo investir em ações?",
    "Qual a previsão do tempo para amanhã?",
]
st.write(" • ".join(f"`{item}`" for item in examples))
