# EXERCÍCIO 7 - CONTAGEM INTELIGENTE

# pedir ao usuário o número inicial da contagem
# pedir ao usuário o número final da contagem
# mostrar na tela um título como "CONTANDO..."
# verificar se a contagem será progressiva
# (ou seja, quando o número inicial é menor que o número final)

    # criar um contador começando no número inicial

    # usar um while para contar até chegar no número final

        # mostrar o número atual da contagem

        # aumentar o contador em 1 a cada repetição

# caso contrário, a contagem será regressiva
# (quando o número inicial é maior que o número final)

    # criar um contador começando no número inicial

    # usar um while para contar até chegar no número final

        # mostrar o número atual da contagem

        # diminuir o contador em 1 a cada repetição

# quando a contagem terminar, mostrar uma mensagem de fim
# exemplo: "Fim da execução"

inicio =  int(input("Digite o número inicial da contagem: "))
fim = int(input("Digite o número final da contagem: "))

print("\nCONTANDO...")
# Verifica se a contagem é progressiva
# (Quando o número inicial é menor que o número final)

if inicio < fim:
    contador = inicio #Criar um contador começando no número inicial
    while contador <= fim:
        print(contador)
        contador = contador + 1 
else:
    contador = inicio
    while contador >= fim:
        print(contador)
        contador = contador - 1

# Quando a contagem terminar
print("Fim da execução")   