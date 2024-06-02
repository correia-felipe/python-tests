# tests/test_classifica_idade.py

import pytest
from src.funcs import classifica_idade

@pytest.mark.parametrize('idade, categoria', [
    (10, 'crianca'),    
    (22, 'adulto'),       
    (80, 'idoso'),       
    #adicionando parametro para demonstrar que dará erro  
    pytest.param('a', None, marks=pytest.mark.xfail(raises=TypeError)) 
])
def test_classifica_idade(idade, categoria):
    assert classifica_idade(idade) == categoria
