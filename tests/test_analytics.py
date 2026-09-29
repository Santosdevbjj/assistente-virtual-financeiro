from assistant.analytics import (
    emergency_reserve_gap,
    expenses_by_category,
    period_balance,
    total_expenses,
    total_income,
)


def test_totals(knowledge):
    assert total_income(knowledge.transactions) == 5000.0
    assert round(total_expenses(knowledge.transactions), 2) == 2488.9
    assert round(period_balance(knowledge.transactions), 2) == 2511.1


def test_expenses_by_category(knowledge):
    values = expenses_by_category(knowledge.transactions)
    assert round(values["moradia"], 2) == 1380.0
    assert round(values["alimentacao"], 2) == 570.0


def test_reserve_gap(knowledge):
    assert emergency_reserve_gap(knowledge.profile) == 5000.0
