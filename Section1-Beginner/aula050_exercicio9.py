"""
Exercício
Exiba os índices da lista
"""
# Minha resolução
# lista = ['Maria', 'Helena', 'Luiz']

# indice = 0

# for nome in lista:
#     print(indice, nome)
#     indice += 1
    
# Resolução do Otavio

lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))