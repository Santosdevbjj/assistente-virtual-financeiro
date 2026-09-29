def test_deterministic_answers(assistant):
    answer = assistant.answer("Quanto gastei com alimentação?")
    assert "570.00" in answer


def test_off_scope_answer(assistant):
    answer = assistant.answer("Qual a previsão do tempo para amanhã?")
    assert "educação financeira" in answer.casefold()


def test_recommendation_answer(assistant):
    answer = assistant.answer("Devo investir em ações?")
    assert "não recomenda" in answer.casefold()
