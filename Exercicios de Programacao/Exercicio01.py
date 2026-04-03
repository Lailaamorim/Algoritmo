# EXERCÍCIO 1 — APTO A DIRIGIR

# Crie um programa para um sistema simples do Departamento de Trânsito.

# O programa deve:

# 1. Mostrar um título na tela: "Departamento de Trânsito".
# 2. Pedir ao usuário que digite o ano de nascimento no formato YYYY.
# 3. O programa deve considerar o ano atual para calcular a idade da pessoa.
# 4. Calcular a idade da pessoa.
# 5. Mostrar na tela o status com a idade da pessoa.

# Depois disso o programa deve verificar:

# - Se a idade for maior ou igual a 18:
#     Mostrar que a pessoa está apta a tirar a carteira de motorista.

# - Caso contrário:
#     Mostrar que a pessoa NÃO está apta a tirar a carteira de motorista.

ano1 = int(input("Digite o ano atual: (YYYY) "))
ano2 = int(input("Digite o ano de seu nascimento: (YYYY) "))
print("DEPARTAMENTO DE TRÂNSITO")
idade = ano1 - ano2
if idade >= 18 :
  print(f"Você tem {idade} anos é está apta a tirar a carteira de motorista.")
else: 
  idade < 18 
  print(f"Você tem {idade} anos, NÃO está apta a tirar a carteira de motorista. ")  


