# =========================================
# DESAFIO 06
# Peça um número inteiro e mostre a tabuada dele.
#
# SAÍDA ESPERADA:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
# =========================================

num = int(input("Digite um número para ver a tabuada dele: "))
for i in range(1,11):
  resultado = num * i
  print(f"{num} X {num} = {num*i}")