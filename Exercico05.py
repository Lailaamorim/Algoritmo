# EXERCÍCIO 5 — RESULTADO DE UMA PARTIDA DE FUTEBOL

# Crie um programa que analise o resultado de uma partida
# entre dois times de futebol.

# O programa deve:

# 1. Mostrar um título: "Analisador de Partida de Futebol".
# 2. Pedir ao usuário:
#    - nome do primeiro time
#    - nome do segundo time
#    - quantidade de gols do primeiro time
#    - quantidade de gols do segundo time

# O programa deve comparar os gols e mostrar o resultado da partida.

# Regras:

# Se os dois times fizerem o mesmo número de gols:
# o resultado é EMPATE.

# Se o primeiro time fizer mais gols:
# o primeiro time é o vencedor.

# Se o segundo time fizer mais gols:
# o segundo time é o vencedor.

# O programa também deve mostrar a diferença de gols entre os times.

print("Analisador de Partida de futebol")

time1 = input("Nome do primeiro time: ").upper()
time2 = input("Nome do segundo time: ").upper()

time1_gols = int(input(f"Quantos gols fez o {time1}?: "))
time2_gols = int(input(f"Quantos gols fez o {time2}?: "))

print(f"\nResultado da partida: {time1} {time1_gols} X {time2_gols} {time2}")

if time1_gols == time2_gols:
  print("A PARTIDA TERMINOU EM EMPATE!!")
elif time1_gols > time2_gols:
  print(f" O {time1} VENCEU!!")
else:
  time2 > time1
  print(f" O {time2} VENCEU!!")
