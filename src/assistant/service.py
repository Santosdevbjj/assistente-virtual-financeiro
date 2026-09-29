from __future__ import annotations

from .analytics import financial_summary
from .guardrails import classify_message, safe_fallback
from .prompts import build_prompt


class FinancialAssistant:
    def __init__(self, knowledge, llm_client=None):
        self.knowledge = knowledge
        self.llm_client = llm_client

    def build_context(self) -> str:
        summary = financial_summary(self.knowledge.transactions, self.knowledge.profile)
        expenses = "\n".join(
            f"- {category}: R$ {value:.2f}"
            for category, value in summary["despesas_por_categoria"].items()
        )
        products = "\n".join(
            f"- {p.nome}: risco={p.risco}; rentabilidade informada={p.rentabilidade}; "
            f"aporte mínimo=R$ {p.aporte_minimo:.2f}; indicado para={p.indicado_para}"
            for p in self.knowledge.products
        )
        return (
            "PERFIL [perfil_investidor.json]\n"
            f"- Nome: {self.knowledge.profile.nome}\n"
            f"- Idade: {self.knowledge.profile.idade}\n"
            f"- Profissão: {self.knowledge.profile.profissao}\n"
            f"- Renda mensal: R$ {self.knowledge.profile.renda_mensal:.2f}\n"
            f"- Perfil informado: {self.knowledge.profile.perfil_investidor}\n"
            f"- Objetivo principal: {self.knowledge.profile.objetivo_principal}\n"
            f"- Patrimônio total informado: R$ {self.knowledge.profile.patrimonio_total:.2f}\n"
            f"- Reserva atual informada: R$ {self.knowledge.profile.reserva_emergencia_atual:.2f}\n\n"
            "MÉTRICAS CALCULADAS [analytics.py + transacoes.csv]\n"
            f"- Receitas do período: R$ {summary['receitas']:.2f}\n"
            f"- Despesas do período: R$ {summary['despesas']:.2f}\n"
            f"- Saldo do período: R$ {summary['saldo_periodo']:.2f}\n"
            f"- Lacuna estimada para a meta de reserva: R$ {summary['lacuna_reserva']:.2f}\n\n"
            f"DESPESAS POR CATEGORIA [transacoes.csv]\n{expenses}\n\n"
            f"PRODUTOS DISPONÍVEIS PARA EXPLICAÇÃO [produtos_financeiros.json]\n{products}\n\n"
            "HISTÓRICO DE ATENDIMENTO [historico_atendimento.csv]\n"
            f"{self.knowledge.history.to_string(index=False)}\n\n"
            "NOTA DE DADOS\nTodos os dados acima são fictícios e fazem parte de um dataset de demonstração."
        )

    def answer(self, question: str) -> str:
        guardrail = classify_message(question)
        if not guardrail.allowed:
            return safe_fallback(guardrail)
        if self.llm_client is None:
            return self.deterministic_answer(question)
        try:
            return self.llm_client.generate(build_prompt(self.build_context(), question))
        except Exception:
            return (
                "Não consegui consultar o modelo local agora. "
                "Posso continuar usando as informações determinísticas da base de demonstração."
            )

    def deterministic_answer(self, question: str) -> str:
        q = question.casefold()
        summary = financial_summary(self.knowledge.transactions, self.knowledge.profile)

        if "quanto gastei com alimentação" in q or "gastei com alimentacao" in q:
            value = summary["despesas_por_categoria"].get("alimentacao", 0)
            return f"Na base de demonstração, alimentação totaliza R$ {value:.2f} no período analisado. [transacoes.csv]"

        if "onde estou gastando" in q or "maior despesa" in q:
            top = list(summary["despesas_por_categoria"].items())[:3]
            details = "; ".join(f"{k}: R$ {v:.2f}" for k, v in top)
            return f"As maiores despesas do período são {details}. [transacoes.csv]"

        if "saldo" in q:
            return f"O saldo do período na base fictícia é R$ {summary['saldo_periodo']:.2f}, calculado como receitas menos despesas. [transacoes.csv]"

        if "reserva" in q:
            p = self.knowledge.profile
            return (
                f"A reserva informada é de R$ {p.reserva_emergencia_atual:.2f}. "
                f"A lacuna até a meta cadastrada é de R$ {summary['lacuna_reserva']:.2f}. "
                "Esses valores são do dataset fictício. [perfil_investidor.json]"
            )

        for product in self.knowledge.products:
            if product.nome.casefold() in q:
                return (
                    f"{product.nome} é descrito na base como um produto de {product.categoria}, "
                    f"com risco {product.risco}, rentabilidade informada de {product.rentabilidade} "
                    f"e aporte mínimo de R$ {product.aporte_minimo:.2f}. "
                    "A descrição é educativa e não constitui recomendação. [produtos_financeiros.json]"
                )

        return (
            "Posso ajudar com gastos, saldo do período, reserva de emergência, metas e explicações "
            "sobre os produtos existentes na base. Para informações que não estejam no dataset, "
            "vou indicar que não tenho dados suficientes."
        )
