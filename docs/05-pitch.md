# 5. Pitch — 3 minutos

O desafio orienta um pitch dividido em problema, solução, demonstração e diferencial/impacto.

## 0:00–0:30 — Problema

> Informações financeiras podem estar organizadas, mas isso não significa que sejam fáceis de entender. O desafio deste projeto foi transformar uma base de transações, perfil, metas e histórico em uma conversa simples, sem permitir que a IA invente dados.

## 0:30–1:30 — Solução

> Eu construí o Nexo, um assistente virtual de educação financeira. Ele usa Streamlit na interface, Python na camada de domínio, dados mockados como base de conhecimento e Ollama como LLM local opcional.
>
> A decisão arquitetural principal foi separar o que precisa ser determinístico do que pode ser generativo. O código calcula receitas, despesas, saldo e indicadores de metas. O modelo fica responsável pela interpretação e pela explicação.
>
> Também existem guardrails para impedir pedidos de recomendação de investimentos, acesso a informações sensíveis e perguntas fora do escopo.

## 1:30–2:30 — Demonstração

Mostrar:

1. dashboard lateral;
2. pergunta sobre gastos;
3. resposta com valor calculado;
4. pergunta sobre produto;
5. tentativa de recomendação;
6. tentativa de obter senha;
7. pergunta fora do escopo.

## 2:30–3:00 — Diferencial e impacto

> O diferencial não é apenas usar IA. É mostrar onde a IA deve entrar e onde ela não deve entrar.
>
> Em um domínio financeiro, o modelo não deve ser a fonte da verdade para cálculos. A aplicação precisa controlar dados, regras e limites. O resultado é um protótipo pequeno, mas com uma arquitetura que deixa claros os caminhos para testes, observabilidade, segurança e evolução para produção.
