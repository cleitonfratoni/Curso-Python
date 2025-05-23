# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

"""
Shalow Copy - Copia rasa. Basicamente copiamos o dicionário e seus valores imutáveis, mas não conseguimos
copiar seus valores mutáveis como uma lista.
"""
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

d2 = copy.copy(d1)

d2['c1'] = 100
d2['l1'][1] = 9999
print(d1)
print(d2)

"""
Deep Copy - Copia profunda. Uma cópia completa do objeto, copiando até mesmo seus submodulos como o listas.
"""

d3 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

d4 = copy.deepcopy(d3)

d4['c1'] = 100
d4['l1'][1] = 9999
print(d3)
print(d4)
