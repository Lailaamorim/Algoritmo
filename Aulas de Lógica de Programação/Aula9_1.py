# EXEMPLO 1 — Mostrar matriz formatada

# Esse código percorre e imprime todos os elementos de uma 
# Matriz (lista de listas) em Python, organizando a saída 
# em formato de tabela.

# Criação de uma matriz (Lista de Listas)
matriz = [
    [1, 2, 3], # Linha 0
    [4, 5, 6]  # Linha 1 
]

# Percorre cada linha da matriz
for i in range(2): # i vai de 0 até 1 (duas linhas)
    # Percorre cada coluna da linha atual
    for j in range(3): # j vai 0 até 2 (três colunas)

        # Acessa o elemento na linha i e coluna j 
        # E imprime na mesma linha, separado por espaço 
        print(matriz[i][j], end=" ") # end=" " evita quebra de linha

    # Após terminar uma linha pula para a próxima linha
    print()     
