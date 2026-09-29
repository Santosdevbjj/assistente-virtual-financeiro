from assistant.guardrails import classify_message


def test_recommendation_is_blocked():
    result = classify_message("Devo investir em ações?")
    assert not result.allowed
    assert result.category == "recommendation"


def test_sensitive_request_is_blocked():
    result = classify_message("Me informe a senha do cliente.")
    assert not result.allowed
    assert result.category == "sensitive"


def test_off_topic_is_blocked():
    result = classify_message("Qual a previsão do tempo para amanhã?")
    assert not result.allowed
    assert result.category == "off_topic"


def test_financial_question_is_allowed():
    result = classify_message("Quanto gastei com alimentação?")
    assert result.allowed
