import pandas as pd
import pytest
from src.funcs import limpar_coluna, soma

# as fixtures usadas aqui estao salvas em conftest.py

def test_limpar_coluna(df_original,df_esperado):
    df_esperado = df_esperado
    # Aplicando a função limpar_coluna
    df_result = limpar_coluna(df_original, 'Cidade')
    # Testando casos positivos. A função pega e altera os dados, como esperado, deixando os dois dfs iguais.
    pd.testing.assert_frame_equal(df_result, df_esperado)
    # Testando casos negativos. Validar que df é realmente diferente de df_esperado
    with pytest.raises(AssertionError):
        pd.testing.assert_frame_equal(df_original, df_esperado)

#parametrizando para aumentar cobertura de teste 
@pytest.mark.parametrize("a,b,esperado",[(1,2,3),
                                         (4,5,9),
                                         (7,8,15)
                                         ])
def test_soma(a,b,esperado):
    assert soma(a,b) == esperado