"""
Lista em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Método úteis: append, insert, pop, del, clear, extend, +
"""
#         01234
#        -54321
string = 'ABCDE'  # 5 caracteres
# print(bool([]))  # falsy
# print( lista, type(lista))

#        0    1      2                 3    4
#       -5   -4     -3                -2   -1
lista = [123, True, 'Cleiton Fratoni', 1.2, []]
lista[-3] = 'Leticia'
print(lista)
print(lista[2], type(lista[2]))