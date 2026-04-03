# EXERCÍCIO 6 — APROVEITAMENTO ESCOLAR

# Crie um programa para calcular o aproveitamento de um aluno.

# O programa deve:

# 1. Mostrar o nome da escola.
# 2. Pedir ao usuário:
#    - nome do aluno
#    - primeira nota
#    - segunda nota
#    - terceira nota
#    - quarta nota

# Depois disso, o programa deve calcular a média das quatro notas.

# Após calcular a média, classifique o aproveitamento
# do aluno usando as seguintes regras:

# média entre 9.0 e 10.0 → conceito A
# média entre 8.0 e 8.9 → conceito B
# média entre 7.0 e 7.9 → conceito C
# média entre 6.0 e 6.9 → conceito D
# média entre 5.0 e 5.9 → conceito E
# média abaixo de 5.0 → conceito F

# O programa deve mostrar:

# nome da escola
# nome do aluno
# média final
# conceito de aproveitamento (A até F)

print("COLEGIO HAMORYM")
print("SISTEMA DE AVALIAÇÃO DO ALUNO")

nome = input("Digite o nome do Aluno(a): ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

# Mostra os dados do aluno
print("\nRESULTADO")
print(f"ALUNO(A): {nome}")
print(f"MÉDIA: {media}")

# Verifica o conceito

if media >= 9.0 and media <= 10.0:
    print("CONCEITO A")
    print("ARRASOU! PARABÉNS PELO EXCELENTE DESEMPENHO, CONTINUE ASSIM!")

elif media >= 8.0 and media <= 8.9:
    print("CONCEITO B")
    print("MUITO BOM! SEU DESEMPENHO FOI ÓTIMO, CONTINUE SE DEDICANDO.")

elif media >= 7.0 and media <= 7.9:
    print("CONCEITO C")
    print("BOM TRABALHO! CONTINUE ESTUDANDO.")

elif media >= 6.0 and media <= 6.9:
    print("CONCEITO D")
    print("RESULTADO RAZOÁVEL, MAS VOCÊ PODE MELHORAR.")

elif media >= 5.0 and media <= 5.9:
    print("CONCEITO E")
    print("FIQUE ATENTO! ESTUDE MAIS.")

else:
    print("CONCEITO F")
    print("VOCÊ PRECISA ESTUDAR MAIS. NÃO DESISTA!")