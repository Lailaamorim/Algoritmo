# O WHILE é usado para criar um laço de repetição em Python.
# Ele executa um bloco de código ENQUANTO uma condição for verdadeira.

# Estrutura básica:
# while condição:
#     código que será repetido

# O programa verifica a condição:
# - Se for VERDADEIRA → o código dentro do while executa
# - Se for FALSA → o programa sai do laço

# Exemplo simples:

contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1

# Explicação do exemplo:
# O contador começa em 1
# Enquanto o contador for menor ou igual a 5 o programa continua repetindo
# A cada repetição o contador aumenta +1
# Quando chegar em 6 a condição fica falsa e o laço termina