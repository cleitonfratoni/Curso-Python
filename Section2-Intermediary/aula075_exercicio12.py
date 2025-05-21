# Exercício
# Crie funções que duplicam, triplicam e quadruplicam
# o numero recebido como parametro

# def double(n1):
#     return n1 * 2

# def triple(n1):
#     return n1 * 3

# def quadruple(n1):
#     return n1 * 4

def create_multiplicator(multiplicator):
    def mult(number):
        return number * multiplicator
    return mult

double = create_multiplicator(2)
triple = create_multiplicator(3)
quadruple = create_multiplicator(4)

print(f"O dobro de 6 é {double(6)}")
print(f"O triplo de 6 é {triple(6)}")
print(f"O quadruplo de 6 é {quadruple(6)}")
