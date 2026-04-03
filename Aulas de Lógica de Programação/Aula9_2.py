# 📌 EXEMPLO 2 — Somar todos os elementos
# criação de uma matriz 2x2 (2 linhas e 2 colunas)
matriz = [
    [1, 2],  # linha 0
    [3, 4]   # linha 1
]

# variável para armazenar a soma total
soma = 0

# percorre as linhas da matriz
for i in range(2):  # i = 0 e 1
    
    # percorre as colunas da matriz
    for j in range(2):  # j = 0 e 1
        
        # adiciona o valor atual da matriz na variável soma
        soma += matriz[i][j]

# imprime o resultado final da soma
print(soma)