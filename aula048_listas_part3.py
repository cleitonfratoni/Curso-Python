"""
Lista em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Método úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop- Remove do final ou do índice escolhido 
    del - Apaga um índice
    clear - Limpa a lista
    extend - estende a lista
    + - Concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Cleiton')
nome = lista.pop()
print(lista,nome)
# lista.clear()
lista.append(1233)
del lista[-1]
lista.insert(0, 5)
print(lista)
print(len(lista))