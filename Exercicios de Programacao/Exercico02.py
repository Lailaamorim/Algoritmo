# EXERCÍCIO 2 — APROVADO OU REPROVADO

# Crie um programa para uma escola que calcula a média de um aluno.

# O programa deve:

# 1. Mostrar um título na tela com o nome da escola.
# 2. Pedir quatro notas do aluno (notas do semestre).
# 3. Calcular a média dessas quatro notas.
# 4. Mostrar a média do aluno na tela.

# Depois disso o programa deve verificar:

# - Se a média for maior ou igual a 7:
#     Mostrar que o aluno está APROVADO.

# - Se a média for menor que 7:
#     Mostrar que o aluno está REPROVADO.
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a dua terceira nota: "))
nota4 = float(input("Digite a sua quarta nota: "))
m  = (nota1 + nota2 + nota3 + nota4)/ 4
if m > 7:
  print(f"PARABENS SUA NOTA FOI {m}, ESTÁ APROVADO!")
elif m >= 5 and m < 7:
    print(f"Foi por pouco, sua media foi de {m} está de RECUPERAÇÃO")
else:
  print(f"Sua nota foi {m} ESTUDE MAIS!")