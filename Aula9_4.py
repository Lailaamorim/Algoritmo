# 📌 EXEMPLO 4 — Mostrar só uma coluna
# criação de uma matriz 3x2 (3 linhas e 2 colunas)
matriz = [
    [10, 20],  # linha 0
    [30, 40],  # linha 1
    [50, 60]   # linha 2
]

# queremos mostrar apenas a coluna 0 (primeira coluna)

# percorre as linhas da matriz
for i in range(3):  # i = 0, 1, 2
    
    # acessa o elemento da coluna 0 em cada linha
    print(matriz[i][0])