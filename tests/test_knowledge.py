def test_knowledge_loads(knowledge):
    assert knowledge.profile.nome == "João Silva"
    assert len(knowledge.transactions) == 10
    assert len(knowledge.history) == 5
    assert len(knowledge.products) == 5


def test_product_lookup(knowledge):
    product = knowledge.product_by_name("CDB Liquidez Diária")
    assert product is not None
    assert product.risco == "baixo"
