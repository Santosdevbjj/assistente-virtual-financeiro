# 2. Base de Conhecimento

## Dados utilizados

| Arquivo | Formato | Utilização |
|---|---|---|
| `historico_atendimento.csv` | CSV | contexto de interações |
| `perfil_investidor.json` | JSON | contexto do cliente fictício |
| `produtos_financeiros.json` | JSON | explicações educativas |
| `transacoes.csv` | CSV | métricas financeiras |

Esses quatro artefatos são exatamente os tipos de dados disponibilizados no desafio. fileciteturn1file3L260-L267

## Qualidade

A aplicação valida:

- presença de colunas obrigatórias;
- datas;
- valores numéricos;
- campos essenciais do perfil;
- schema dos produtos.

## Estratégia de integração

Na inicialização:

1. CSVs são carregados com pandas.
2. JSONs são validados com Pydantic.
3. Métricas são calculadas deterministicamente.
4. Um contexto textual controlado é montado.
5. O contexto é enviado ao LLM apenas quando `LLM_ENABLED=true`.

## Por que não colocar tudo no system prompt?

O material do desafio mostra a injeção direta de dados como abordagem simples, mas observa que uma solução mais robusta pode consultar informações dinamicamente. fileciteturn2file12L719-L722

Neste protótipo, o contexto é montado por uma camada intermediária para evitar que a interface ou o modelo manipulem diretamente os arquivos.

## Exemplo de contexto

```text
PERFIL
Nome: João Silva
Perfil informado: moderado
Objetivo: Construir reserva de emergência

MÉTRICAS CALCULADAS
Receitas: R$ 5000,00
Despesas: R$ 2488,90
Saldo: R$ 2511,10

DESPESAS POR CATEGORIA
moradia: R$ 1380,00
alimentacao: R$ 570,00
...
```

## Observação temporal

Os dados fornecidos são de demonstração. Datas do dataset não devem ser interpretadas como saldo atual ou situação financeira atual da pessoa.
