from __future__ import annotations
import pandas as pd


def total_income(transactions: pd.DataFrame) -> float:
    return float(transactions.loc[transactions["tipo"].eq("entrada"), "valor"].sum())


def total_expenses(transactions: pd.DataFrame) -> float:
    return float(transactions.loc[transactions["tipo"].eq("saida"), "valor"].sum())


def period_balance(transactions: pd.DataFrame) -> float:
    return total_income(transactions) - total_expenses(transactions)


def expenses_by_category(transactions: pd.DataFrame) -> pd.Series:
    expenses = transactions.loc[transactions["tipo"].eq("saida")]
    return expenses.groupby("categoria")["valor"].sum().sort_values(ascending=False)


def emergency_reserve_gap(profile) -> float:
    target = next(
        (m["valor_necessario"] for m in profile.metas if "reserva" in m["meta"].casefold()),
        profile.reserva_emergencia_atual,
    )
    return max(float(target) - float(profile.reserva_emergencia_atual), 0.0)


def financial_summary(transactions: pd.DataFrame, profile) -> dict:
    by_category = expenses_by_category(transactions)
    return {
        "receitas": total_income(transactions),
        "despesas": total_expenses(transactions),
        "saldo_periodo": period_balance(transactions),
        "despesas_por_categoria": by_category.to_dict(),
        "lacuna_reserva": emergency_reserve_gap(profile),
    }
