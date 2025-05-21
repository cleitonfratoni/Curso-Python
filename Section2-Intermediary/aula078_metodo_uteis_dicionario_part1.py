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
pessoa = {
    'nome': 'Cleiton Fratoni',
    'sobrenome': 'Rocha',
}

pessoa.setdefault('idade', None)
print(pessoa['idade'])
# print(f"Exemplo de len: {len(pessoa)}")
# print(f"Exemplo de keys: {list(pessoa.keys())}")
# print(f"Exemplo de values: {list(pessoa.values())}")
# print(f"Exemplo de items: {list(pessoa.items())}")

# for chave, valor in pessoa.items():
#     print(chave, valor)