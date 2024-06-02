'''
Suponha que temos uma função chamada classifica_idade que categoriza a 
idade de uma pessoa em 'criança', 'adolescente', 'adulto' ou 'idoso'. 
A tarefa é escrever testes para essa função utilizando markers para diferenciar os testes baseados em categorias de idade.
'''
import pytest
from src.tests.exercises.exerc3 import classifica_idade

@pytest.mark.crianca
def test_classifica_idade_crianca():
    assert classifica_idade(12) ==  'crianca'

@pytest.mark.adulto
def test_classifica_idade_adulto():
    assert classifica_idade(25) ==  'adulto'

@pytest.mark.idoso
def test_classifica_idade_idoso():
    assert classifica_idade(72) ==  'idoso'

'''
criei os testes, um pra cada categoria de idade e criei o marcador em pytest.ini
'''