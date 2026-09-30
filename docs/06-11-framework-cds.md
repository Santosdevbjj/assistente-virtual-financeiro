# Framework CDS — 11 passos adaptados ao projeto

O material apresenta uma estrutura que transforma uma análise/projeto de dados em uma narrativa de problema, evidência, solução, performance e produção. Para este projeto de IA generativa, os passos foram adaptados sem fingir que existe treinamento de modelo próprio.

## 1. Problema de negócio

Transformar dados financeiros fictícios em educação financeira contextualizada, reduzindo o risco de respostas inventadas.

## 2. Baseline

Chatbot simples com dados inseridos no contexto do LLM.

## 3. Planejamento da solução

Stack:

- Python;
- Streamlit;
- pandas;
- Pydantic;
- Ollama;
- pytest;
- GitHub Actions.

## 4. Limpeza de dados

Validação de schema, tipos, datas, valores e campos obrigatórios.

## 5. EDA

A análise descritiva responde:

- quanto entrou;
- quanto saiu;
- onde houve mais gastos;
- qual é o saldo do período;
- qual é a lacuna da meta de reserva.

## 6. Preparação

Os dados são convertidos em objetos tipados e em métricas determinísticas antes de entrar no contexto do LLM.

## 7. "Treinamento"

Não há treinamento de modelo neste projeto.

A etapa correspondente é **configuração e avaliação de comportamento**, por meio de system prompt, exemplos, guardrails e testes.

Não seria correto afirmar que o projeto treinou um modelo próprio.

## 8. Performance

Performance funcional:

- testes automatizados;
- assertividade;
- segurança;
- coerência.

Performance operacional futura:

- latência;
- tokens;
- custo;
- erros.

## 9. Business Performance

O valor demonstrado não é uma promessa financeira.

O ganho é operacional/educacional: transformar dados dispersos em explicações contextualizadas e reduzir o risco de o LLM gerar números que deveriam vir do sistema.

## 10. Modelo em produção

No protótipo:

```text
Streamlit → FinancialAssistant → Guardrails → KnowledgeBase
                                          ├→ Analytics
                                          └→ Ollama
```

Em uma evolução:

```text
Web/App → API → Auth → Domain Services
                     ├→ Knowledge Store
                     ├→ Financial Tools
                     ├→ LLM Gateway
                     ├→ Guardrails
                     └→ Observability
```

## 11. Storytelling

O pitch mostra:

**problema → decisão → arquitetura → demonstração → limites → evolução**.

Isso evita transformar o projeto em uma lista de ferramentas.
