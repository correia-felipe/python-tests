
def is_positive(numero):
    return numero > 0

def limpar_coluna(df, coluna):
    #fazendo o copy para nao alterar o original
    df_copy = df.copy()
    df_copy[coluna] = df_copy[coluna].str.strip().str.lower()
    return df_copy 

def soma(a,b):
    return a + b

def multiplicacao(a,b):
    return a * b

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
    
def calcula_total(preco,desconto, taxa):
    valor_desconto = preco * desconto
    valor_taxa = (preco - valor_desconto) * taxa
    total = preco - valor_desconto + valor_taxa
    return total 

