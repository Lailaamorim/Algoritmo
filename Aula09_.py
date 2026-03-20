# ==========================================================
# MATRIZES EM PYTHON (EXPLICAÇÃO SIMPLES)
# ==========================================================

# Uma matriz é como uma tabela com LINHAS e COLUNAS.
# Pense em uma planilha do Excel ou uma tabela de notas.

# Exemplo de tabela:

#        Coluna0 Coluna1 Coluna2
# Linha0    10      20      30
# Linha1    40      50      60
# Linha2    70      80      90

# Isso é uma matriz 3x3 (3 linhas e 3 colunas).

# Em Python, uma matriz é criada usando LISTAS dentro de LISTAS.

matriz = [
    [10, 20, 30],   # linha 0
    [40, 50, 60],   # linha 1
    [70, 80, 90]    # linha 2
]

# ==========================================================
# COMO ACESSAR UM VALOR NA MATRIZ
# ==========================================================

# Para acessar um valor usamos:
# matriz[linha][coluna]

print(matriz[0][0])  # linha 0 coluna 0 → 10
print(matriz[1][2])  # linha 1 coluna 2 → 60
print(matriz[2][1])  # linha 2 coluna 1 → 80

# ==========================================================
# PERCORRENDO UMA MATRIZ
# ==========================================================

# Para percorrer todos os valores da matriz usamos DOIS FOR
# Um for percorre as linhas
# Outro for percorre as colunas

for linha in matriz:
    for valor in linha:
        print(valor)

# ==========================================================
# DIFERENÇA ENTRE VETOR E MATRIZ
# ==========================================================

# Vetor → lista simples (uma dimensão)
numeros = [10, 20, 30, 40]

# Matriz → lista de listas (duas dimensões)
numeros_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Vetor usa apenas um índice
print(numeros[2])  # 30

# Matriz usa dois índices
print(numeros_matriz[1][2])  # 6

# ==========================================================
# RESUMO
# ==========================================================

# Vetor = lista de valores
# Exemplo:
# [10, 20, 30]

# Matriz = tabela com linhas e colunas
# Exemplo:
# [10, 20, 30]
# [40, 50, 60]
# [70, 80, 90]

# Vetor → 1 dimensão
# Matriz → 2 dimensões