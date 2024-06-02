'''
Suponha que você tenha a seguinte função em um módulo Python, 
que calcula o fatorial de um número inteiro não negativo:
Sua tarefa é escrever testes parametrizados para essa função, 
cobrindo vários casos, como o fatorial de 0, 1, um número positivo 
e talvez um caso que lance uma exceção para entradas inválidas, como números negativos.
'''

def fatorial_(n):
    if n < 0:
        raise ValueError("Entrada inválida: n deve ser um número inteiro não negativo.")
    if n == 0:
        return 1
    else:
        return n * fatorial_(n-1)