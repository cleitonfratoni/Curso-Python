"""
Faça uma lista de comprar ocm listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os
from curses.ascii import isdigit

lista_compras = []
opcao = ''
opcao_selcionada = 0

while True:
    print(
        f'ESCOLHA UMA DAS OPÇÕES\n\
          1 - Adicionar item na lista de compras\n\
          2 - Remover intem na lista de compras\n\
          3 - Listar itens da sua lista\n\
          4 - Sair do programa'
    )
    opcao = input('Digite sua opção: ')
    
    try:
        opcao.isdigit()
        opcao_selcionada = int(opcao)
    
        if opcao_selcionada == 1:
            lista_compras.append(input('Digite o item que deseja adicionar a lista: '))
            os.system("clear")
            print(f'O item {lista_compras[-1]} foi adcionado a lista com sucesso!')
        elif opcao_selcionada == 2:
            rm_indice = input('Digite o indice que deseja apagar: ')
            rm_indice = int(rm_indice)
            os.system("clear")
            try:
                lista_compras.pop(rm_indice)
                print('Item removido com sucesso!')
            except:
                print('Indice inexistente')
        elif opcao_selcionada == 3:
            os.system("clear")
            for indice, nome in enumerate(lista_compras):
                print('LISTA DAS SUAS COMPRAS')
                print(indice,nome)
            if lista_compras == []:
                print('Não há nada na lista')
                
        elif opcao_selcionada == 4:
            print('Finalizando programa.')
            break
        else:
            os.system("clear")
            print('Opção invalida! Favor digitar alguma das opções sugeridas.')
    except:
        os.system("clear")
        print('Opção invalida! Favor digitar alguma das opções sugeridas.')