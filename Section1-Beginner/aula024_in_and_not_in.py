# Operadores in e noit in
# Strings são iteráveis
#  0 1 2 3 4 5 6
#  C l e i t o n
# -7-6-5-4-3-2-1

# nome = 'Cleiton'
# # print(nome[2])
# # print(nome[-2]) 
# print('ton' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('ton' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')