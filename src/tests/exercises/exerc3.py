'''
Suponha que temos uma função chamada classifica_idade que categoriza a 
idade de uma pessoa em 'criança', 'adolescente', 'adulto' ou 'idoso'. 
A tarefa é escrever testes para essa função utilizando markers para diferenciar os testes baseados em categorias de idade.
'''

def classifica_idade(idade):
    if not isinstance(idade, (int, float)):
        raise TypeError("Idade deve ser um número.")
    if idade <= 12:
        return 'crianca'
    elif  idade < 18:
        return 'adolescente'
    elif 18 <= idade < 60:
        return 'adulto' 
    else:
        return 'idoso'