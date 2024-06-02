from src.funcs import soma, multiplicacao
import time 
import pytest 
'''
usando marcador no teste para executar somente os que acompetem ao tema. 
para evitar warning, podemos adicionar no pytest.ini o nome dos marcadores que iremos utilizar no projeto. 
para executar apenas os testes que queremos, usamos:
pytest -v test_soma_multiplicacao.py -m 'lento'
OU
pytest -v test_soma_multiplicacao.py -m 'not lento' para retirar esses topicos
OU 
pytest -v test_soma_multiplicacao.py -m 'rapido or lento' para executar varios marcadores
OU 
pytest -v test_soma_multiplicacao.py -k 'lento' para executar marcadores que contenham a string 'lento' em seu nome.
'''
@pytest.mark.rapido
def test_soma():
    assert soma(2,2) == 4 

@pytest.mark.lento
def test_soma_lento():
    time.sleep(2)
    assert soma(3,2) == 5

@pytest.mark.rapido
def test_multiplicacao():
    assert multiplicacao(2,1) == 2  

@pytest.mark.lento
def test_multiplicacao_lento():
    time.sleep(2)
    assert multiplicacao(2,5) == 10

#esse abaixo temos os dois. ele irá executar conforme chamado esses dois topicos. 
@pytest.mark.lento
@pytest.mark.rapido
def test_multiplicacao_ambos():
    time.sleep(2)
    assert multiplicacao(2,5) == 10
