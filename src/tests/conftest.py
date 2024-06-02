'''
SCOPES:
    Function
        - Padrão. Criada e destruída após alguma função de teste a utilizar. 
    Class
        - Criada e destruida para cada instancia de uma classe que a utilizar. Todos os testes usarão a mesma instancia da fixture 
    Module 
        - Criada e destruida para cada vez que o modulo/arquivo de teste a utilizar e.g spark session é ideal aqui nesse escopo. 
    Package 
        - Criada e destruida para cada package que a utilizar. 
    Session 
        - Toda sessao de teste compartilha a mesma fixture. Aqui tbm caberia o spark session(?)
'''

#criando uma fixture, que pode ser considerado arquivos de configuracao de entrada em nossos processos. 
import pytest
import pandas as pd 
#from pyspark.sql import SparkSession


@pytest.fixture
def df_original():
    data = {
        'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
        'Idade': [23, 35, 45, 28],
        'Cidade': [' São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
    }
    return pd.DataFrame(data)

@pytest.fixture
def df_esperado():
    data_assert = {
        'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
        'Idade': [23, 35, 45, 28],
        'Cidade': ['são paulo', 'rio de janeiro', 'belo horizonte', 'curitiba']
    }
    return pd.DataFrame(data_assert)




# @pytest.fixture(scope="module")
# def spark():
#     return SparkSession.builder.master("local").appName("PySparkTest").getOrCreate()

# @pytest.fixture
# def df_original(spark):
#     data = [
#         ('Ana', 23, ' São Paulo'),
#         ('Bruno', 35, 'Rio de Janeiro'),
#         ('Carla', 45, 'Belo Horizonte'),
#         ('Daniel', 28, 'Curitiba')
#     ]
#     columns = ['Nome', 'Idade', 'Cidade']
#     return spark.createDataFrame(data, columns)

# @pytest.fixture
# def df_esperado(spark):
#     data_assert = [
#         ('Ana', 23, 'são paulo'),
#         ('Bruno', 35, 'rio de janeiro'),
#         ('Carla', 45, 'belo horizonte'),
#         ('Daniel', 28, 'curitiba')
#     ]
#     columns = ['Nome', 'Idade', 'Cidade']
#     return spark.createDataFrame(data_assert, columns)