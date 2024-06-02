import pytest 
from src.funcs import calcula_total

@pytest.mark.parametrize('preco',[100.00,10.000,10.00])
@pytest.mark.parametrize('desconto',[0.1,0.1,0.0])
@pytest.mark.parametrize('taxa',[0.01,0.1,0.0])
def test_calcula_total(preco, desconto, taxa):
    desconto_esperado = preco * desconto 
    taxa_esperada = (preco - desconto_esperado) * taxa
    total_esperado = preco - desconto_esperado + taxa_esperada

    assert calcula_total(preco, desconto, taxa) == round(total_esperado,2)