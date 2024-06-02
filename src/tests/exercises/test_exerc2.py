from src.tests.exercises.exerc2 import *
import pytest
'''
Suponha que você tenha a seguinte função em um módulo Python, 
que calcula o fatorial de um número inteiro não negativo:
Sua tarefa é escrever testes parametrizados para essa função, 
cobrindo vários casos, como o fatorial de 0, 1, um número positivo 
e talvez um caso que lance uma exceção para entradas inválidas, como números negativos.
'''
@pytest.mark.parametrize("n, expected", [
    (0, 1),                    
    (1, 1),                   
    (5, 120),                  
    (10, 3628800),             
    pytest.param(-1, None, marks=pytest.mark.xfail(raises=ValueError)),  # Caso que deve falhar com ValueError
    pytest.param(-10, None, marks=pytest.mark.xfail(raises=ValueError)), # Outro caso que deve falhar com ValueError
])
def test_fatorial(n, expected):
    if expected is None:
        with pytest.raises(ValueError, match="Entrada inválida: n deve ser um número inteiro não negativo."):
            fatorial_(n)
    else:
        assert fatorial_(n) == expected
        