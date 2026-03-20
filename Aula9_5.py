# 📌 EXEMPLO 5 — Multiplicar todos os valores por 2
# criação de uma matriz 2x2
matriz = [
    [1, 2],  # linha 0
    [3, 4]   # linha 1
]

# percorre todas as linhas e colunas da matriz
for i in range(2):      # i = 0, 1 (linhas)
    for j in range(2):  # j = 0, 1 (colunas)
        
        # multiplica cada elemento por 2
        matriz[i][j] *= 2

# mostrar o resultado final
for linha in matriz:
    # imprime cada linha completa
    print(linha)