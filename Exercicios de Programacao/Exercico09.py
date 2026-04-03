# EXERCÍCIO 09 - MENU DE CONTAGEM

# criar um menu com três opções
# 1 ... contar de 1 até 10 (mostrar os números um do lado do outro)
# 2 ... contar de 10 até 1 (mostrar os números um do lado do outro)
# 3 ... sair do programa

# pedir para o usuário escolher uma opção

# se escolher 1
# fazer uma contagem de 1 até 10
# mostrar os números com ... entre eles para ficarem na mesma linha
# exemplo: 1 ... 2 ... 3 ... 4 ... 5 ... 6 ... 7 ... 8 ... 9 ... 10

# se escolher 2
# fazer uma contagem de 10 até 1
# mostrar os números com ... entre eles para ficarem na mesma linha
# exemplo: 10 ... 9 ... 8 ... 7 ... 6 ... 5 ... 4 ... 3 ... 2 ... 1

# se escolher 3
# mostrar uma mensagem de saída
# encerrar o programa

# o menu deve continuar aparecendo até o usuário escolher sair



opcao = 0
while opcao != 3: # Enquanto a opção for diferente de 3 o menu continua aparecendo
    print(20*"==")
    print("MENU DE CONTAGEM")
    print(20*"==")
    print("[1] - Contar de 1 até 10")
    print("[2] - Contar de 10 até 1")
    print("[3] - Sair do programa")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        contador = 1
        while contador <= 10:
            print(contador, end="...") # end="=" faz com que os números sejam mostrados na mesma linha, separados por "..."
            contador = contador + 1

            print() # Pula para a próxima linha após mostrar os números

    elif opcao == 2:
        contador = 10 # Cria um contador começando do 10
        while contador >= 1:
            print(contador , end="...") # Mostra os números um do lado do outro
            contador = contador - 1 # Diminuindo contador em 1 

            print() # Pula para a próxima linha após mostrar os números


    elif opcao == 3: 
        print("Saindo do programa...")
    else:
        print("Opção invalida. por favor escolha uma opção válida!")    