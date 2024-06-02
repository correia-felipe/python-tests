from src.tests.exercises.exerc1 import *
import pytest

#valor esperado
def test_soma_dobro(lista_dobros):
    assert soma_dobro(lista_dobros) == 12

#acusando erro
def test_soma_dobro_exception(lista_dobros):
    with pytest.raises(AssertionError):
        assert soma_dobro(lista_dobros) == 14