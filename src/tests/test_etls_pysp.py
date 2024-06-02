# import pytest
# from src.funcs import limpar_coluna

# def test_limpar_coluna(df_original, df_esperado):
#     # Aplicando a função limpar_coluna
#     df_result = limpar_coluna(df_original, 'Cidade')
    
#     # Testando casos positivos. A função pega e altera os dados, como esperado, deixando os dois dfs iguais.
#     assert df_result.collect() == df_esperado.collect()
    
#     # Testando casos negativos. Validar que df_original é realmente diferente de df_esperado
#     with pytest.raises(AssertionError):
#         assert df_original.collect() == df_esperado.collect()