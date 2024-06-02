'''
Vamos supor que você tenha uma função chamada soma_dobro em um módulo de Python. 
Essa função recebe uma lista de números, dobra cada número e retorna a soma de todos os números dobrados. 
Sua tarefa é escrever testes para essa função usando uma fixture para criar a lista de entrada antes de cada teste.
'''
def soma_dobro(numeros):
    return sum(x * 2 for x in numeros)
