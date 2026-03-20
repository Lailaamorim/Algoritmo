# criação de uma matriz 2x3 (2 linhas e 3 colunas)
matriz = [
    [10, 20, 30],  # linha 0
    [40, 50, 60]   # linha 1
]

# queremos mostrar apenas a linha 1 (segunda linha)

# percorre as colunas da linha escolhida
for j in range(3):  # j = 0, 1, 2
    
    # acessa os elementos da linha 1 variando a coluna
    print(matriz[1][j])