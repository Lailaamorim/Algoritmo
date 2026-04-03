# EXERCÍCIO 11 - SEQUÊNCIA DE FIBONACCI

# A sequência de Fibonacci funciona assim:
# Cada número é a soma dos dois números anteriores.
# Exemplo: 0, 1, 1, 2, 3, 5, 8, 13...

print("-"*30)
print("SEQUÊNCIA DE FIBONACCI")
print("-"*30)

# quantidade de números
quantidade = 15

# primeiros números da sequência
n1 = 0
n2 = 1

# contador
contador = 0

# loop
while contador < quantidade:

    print(n1)

    proximo = n1 + n2
    n1 = n2
    n2 = proximo

    contador = contador + 1