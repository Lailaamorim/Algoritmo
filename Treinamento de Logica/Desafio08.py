# =========================================
# DESAFIO 08 - ACESSO AO SISTEMA
#
# Faça um programa que peça ao usuário:
# - Um nome de usuário
# - Uma senha
#
# O programa deve verificar:
#
# SE:
# usuário = "admin"
# senha = "1234"
#
# Mostre:
# "Acesso permitido"
#
# SENÃO:
# Mostre:
# "Acesso negado"
#
# =========================================
senha_correta = 1234
usuario_correto = "admin"

print("="*50)
print("ACESSO AO SISTEMA")
print("="*50)
usuario = input("Digite o nome de Usúario: ")
senha = int(input("Digite a senha com 4 digitos: "))

if usuario != usuario_correto or senha != senha_correta:
  print("ACESSO NEGADO ")
else:
  print("ACESSO LIBERADO")  