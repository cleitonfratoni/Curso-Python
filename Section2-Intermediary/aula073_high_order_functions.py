"""
Higher Order Functions
Funções de primeira classe
"""
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

saudacao_2 = saudacao

print(
    executa(saudacao_2, 'Bom dia', 'Cleiton')
)
print(
    executa(saudacao_2, 'Bom dia', 'Leticia')
)