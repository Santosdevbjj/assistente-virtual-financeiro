# Decisões Técnicas e Trade-offs

## Decisão 1 — LLM local

**Escolha:** Ollama.

**Alternativa:** API de LLM hospedada.

**Motivo:** o desafio trabalha com dados financeiros, mesmo fictícios, e a execução local deixa claro o limite de exposição.

**Trade-off:** exige instalação e hardware local.

## Decisão 2 — Cálculo fora do LLM

**Escolha:** pandas/Python.

**Alternativa:** pedir ao modelo para calcular.

**Motivo:** números financeiros devem ser reproduzíveis.

**Trade-off:** mais código de domínio, porém mais testabilidade.

## Decisão 3 — Guardrails determinísticos

**Escolha:** regex + categorias.

**Alternativa:** classificação pelo LLM.

**Motivo:** políticas críticas ficam observáveis e testáveis.

**Trade-off:** regras simples podem não cobrir toda linguagem natural.

## Decisão 4 — Sem framework de agentes

**Escolha:** orquestração própria.

**Motivo:** o fluxo inicial é curto.

**Quando mudar:** múltiplas ferramentas, memória persistente, RAG, roteamento complexo ou necessidade de tracing específico.

## Decisão 5 — Streamlit

**Escolha:** Streamlit.

**Motivo:** entrega rápida de protótipo.

**Quando mudar:** autenticação, múltiplos usuários, SLA, API pública ou frontend separado.
