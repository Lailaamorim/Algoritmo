# ==========================================================
# VETORES EM PYTHON (EXPLICAÇÃO SIMPLES)
# ==========================================================

# Vetores em Python são chamados de LISTAS.

# Um vetor é uma estrutura que guarda vários valores
# dentro de uma única variável.

# Pense em um vetor como várias "caixinhas" guardando valores.

# Exemplo visual de um vetor:

# Posição (índice)
#   0   1   2   3
# [10][20][30][40]

# Cada valor tem uma posição chamada ÍNDICE.

# IMPORTANTE:
# Em Python os índices começam em 0.

# ==========================================================
# CRIANDO UM VETOR
# ==========================================================

# Criando um vetor com alguns números

numeros = [10, 20, 30, 40]

# Mostrando o vetor inteiro
print(numeros)

# ==========================================================
# ACESSANDO VALORES DO VETOR
# ==========================================================

# Para acessar um valor usamos:
# nome_do_vetor[indice]

print(numeros[0])  # primeiro valor → 10
print(numeros[1])  # segundo valor → 20
print(numeros[2])  # terceiro valor → 30
print(numeros[3])  # quarto valor → 40

# ==========================================================
# ALTERANDO VALORES NO VETOR
# ==========================================================

# Podemos mudar um valor do vetor usando o índice.

numeros[1] = 50

# Agora o vetor ficou:
# [10, 50, 30, 40]

print(numeros)

# ==========================================================
# ADICIONANDO VALORES NO VETOR
# ==========================================================

# Podemos adicionar novos valores usando append()

numeros.append(60)

# O vetor agora será:
# [10, 50, 30, 40, 60]

print(numeros)

# ==========================================================
# PERCORRENDO UM VETOR
# ==========================================================

# Para percorrer todos os valores usamos um FOR

for numero in numeros:
    print(numero)

# O programa vai mostrar todos os valores do vetor.

# ==========================================================
# EXEMPLO REAL (LISTA DE ALUNOS)
# ==========================================================

alunos = ["Ana", "Pedro", "Maria", "João"]

for aluno in alunos:
    print("Aluno:", aluno)

# ==========================================================
# RESUMO
# ==========================================================

# Vetor = lista de valores guardados em uma variável.

# Exemplo de vetor:
# [10, 20, 30, 40]

# Cada valor tem um índice (posição).

# Índices começam em 0.

# Exemplo:
# numeros[0] → primeiro valor
# numeros[1] → segundo valor
# numeros[2] → terceiro valor