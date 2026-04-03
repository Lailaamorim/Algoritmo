# EXERCÍCIO 08 - CADASTRO DE ALUNOS

# mostrar o nome da escola

# perguntar quantos alunos a turma tem

# criar um contador começando em 1

# enquanto o contador for menor ou igual à quantidade de alunos

    # mostrar na tela "ALUNO" e o número do aluno

    # pedir o nome do aluno

    # pedir a nota do aluno

    # mostrar o nome e a nota do aluno digitados

    # mostrar uma linha de separação para organizar

    # aumentar o contador para passar para o próximo aluno

print("-"*20) # linha de separação para organizar
print("ESCOLA HAMORYM")
print("-"*20) # linha de separação para organizar

# Pergunta quantos alunos tem na turma
quantidade =  int(input("Quantos alunos tem na turma? "))
contador = 1

# Listas para guardar dados
nomes = []
notas = []

# Repete enquanto NÃO chegar na quantidade de alunos
while contador <= quantidade: 
    print(f"\nALUNO {contador}") 
    nome = input("Digite o nome do aluno(a): ")
    nota = float(input("Digite a nota de aluno(a): "))

    # Guardar dados nas listas
    nomes.append(nome)
    notas.append(nota)

    print(f"Nome do aluno(a): {nome}")
    print(f"Nota do aluno(a): {nota:.2f}")

    print("-"*20) # linha de separação para organizar

    # Proximo Aluno
    contador = contador + 1

# Junta nome e nota
alunos = list(zip(nomes, notas))

# Ordenar por nome (Ordem alfabética)
alunos.sort() # sort() é uma função que organiza (ordena) os elementos de uma lista.

print("\nLISTA DE ALUNOS")
print("-"*20)

for nome, nota in alunos:
    print(f"{nome}: - {nota:.2f}")



# Listas para guardar dados
# nomes = []
# notas = []

# nomes = []
# cria uma lista vazia chamada "nomes".
# uma lista é uma estrutura que guarda vários valores.
# aqui vamos guardar o nome de cada aluno.

# exemplo depois de cadastrar alguns alunos:
# nomes = ["Ana", "Bruno", "Carlos"]

# notas = []
# cria uma lista vazia chamada "notas".
# essa lista vai guardar as notas dos alunos.

# exemplo depois de cadastrar alguns alunos:
# notas = [8.5, 7.0, 9.2]

# durante o programa usamos .append() para adicionar novos dados.
# exemplo:
# nomes.append(nome)
# notas.append(nota)

# assim cada nome e cada nota ficam armazenados
# para serem usados depois no final do programa.


    