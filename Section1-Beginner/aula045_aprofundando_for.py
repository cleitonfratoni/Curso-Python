"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Cleiton'

# iterador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break
    
for letra in texto:
    print(letra)