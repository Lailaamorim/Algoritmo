# Aqui se quer fazer uma lista onde o usúario digite os nomes
alunos = []

for i in range (4):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)

# Monstrando os alunos 
for aluno in alunos:    
    print("Aluno: ", aluno)