# Programa que pede 5 números, soma eles
# e mostra o maior e o menor valor digitado

contador = 1   # variável que controla quantas vezes o loop vai repetir
soma = 0       # variável que vai guardar a soma de todos os números

# loop que vai repetir enquanto o contador for menor ou igual a 5
while contador <= 5:

    # pede um número ao usuário
    # float permite digitar números com decimal
    numero = float(input(f"Digite o {contador}º número: "))

    # se for o primeiro número digitado
    # ele será usado como base para maior e menor
    if contador == 1:
        maior = numero
        menor = numero
    
    else:
        # verifica se o número digitado é maior que o maior atual
        if numero > maior:
            maior = numero   # atualiza o maior número
        
        # verifica se o número digitado é menor que o menor atual
        if numero < menor:
            menor = numero   # atualiza o menor número

    # adiciona o número digitado na soma total
    soma = soma + numero

    # aumenta o contador em 1 para pedir o próximo número
    contador = contador + 1


# mostra os resultados depois que o loop termina
print("\nResultado:")

# mostra a soma de todos os números digitados
print(f"Soma dos números: {soma}")

# mostra qual foi o maior número digitado
print(f"Maior número: {maior}")

# mostra qual foi o menor número digitado
print(f"Menor número: {menor}")