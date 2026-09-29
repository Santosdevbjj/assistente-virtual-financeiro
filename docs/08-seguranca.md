# Segurança, Privacidade e Anti-Alucinação

## Modelo de ameaça simplificado

### Risco: alucinação factual

**Controle:** fatos financeiros calculados pelo código.

### Risco: prompt injection

**Controle atual:** o prompt trata o contexto como controlado e os guardrails limitam categorias conhecidas.

**Limitação:** não é uma proteção completa contra todos os ataques de prompt injection.

### Risco: vazamento de credenciais

**Controle:** o dataset não contém credenciais e mensagens com padrões de senha/token são bloqueadas.

### Risco: recomendação indevida

**Controle:** pedidos de recomendação são bloqueados.

### Risco: confundir dado fictício com dado real

**Controle:** interface, prompt e respostas indicam que os dados são de demonstração.

## Produção

Antes de qualquer uso real seriam necessários, no mínimo:

- autenticação;
- autorização;
- gestão de segredos;
- criptografia;
- logs sem dados sensíveis;
- retenção e descarte;
- revisão jurídica/compliance;
- controles de acesso;
- monitoramento;
- avaliação de modelo;
- testes de segurança;
- revisão humana para fluxos de risco.

O projeto não afirma atender requisitos regulatórios de uma instituição financeira.
