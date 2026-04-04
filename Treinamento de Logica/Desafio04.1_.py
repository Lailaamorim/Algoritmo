# =========================================
# DESAFIO - MÉDIA DO ALUNO
#
# Peça ao usuário 4 notas:
# primeira, segunda, terceira e quarta nota.
#
# Calcule a média dessas notas.
#
# Depois mostre:
# - A média final do aluno
# - A situação dele:
#
# REGRAS:
# Se média ≥ 7 → "Você foi aprovado"
# Se média entre 5 e 6.9 → "Você está de recuperação"
# Se média < 5 → "Você foi reprovado"
# =========================================

n1 = float(input("Digite a Primeira Nota: "))
n2 = float(input("Digite a Segunda Nota: "))
n3 = float(input("Digite a Terceira Nota: "))
n4 = float(input("Digite a Quarta Nota: "))

m = (n1 + n2 + n3 + n4) / 4

if m > 7: 
  print(f"Sua média foi {m}")
  print("PARABÉNS VOCÊ FOI APROVADO!!")
elif m < 6 and m > 5:
  print(f"Sua media foi {m}")
  print("ESTÁ DE RECUPERAÇÃO!")  
else:
  print(f"Sua média foi {m}")    
  print("VOCÊ FOI REPROVADO!!")