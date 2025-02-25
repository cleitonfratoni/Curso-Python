# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

multiplicacao = multiplica(2, 5, 10, 15, 25)

print(multiplicacao)

# Crie uma função fala se um número e par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(x):
    resto = x % 2
    
    if resto == 0:
        return f"{x} é par"
    return f"{x} é ímpar"

print(par_ou_impar(42))
print(par_ou_impar(3))
print(par_ou_impar(15))
print(par_ou_impar(28))