# WHILE TRUE

# Essa estrutura é usada quando não sabemos
# quantas vezes o programa vai repetir.

# "True" significa verdadeiro.
# Então o while True cria um loop que pode repetir para sempre.

# Para parar o loop usamos "break".

# Exemplo:

while True:  # repete para sempre
    numero = int(input("Digite um número (0 para parar): "))

    if numero == 0:  # se o número for 0
        break        # o programa sai do loop

    print("Você digitou:", numero)

# quando o usuário digitar 0 o programa termina