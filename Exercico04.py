# EXERCÍCIO 4 — REAJUSTE DE SALÁRIO

# Crie um programa para calcular o novo salário de um funcionário
# com base na quantidade de dependentes (filhos).

# O programa deve:

# 1. Mostrar um título na tela: "Sistema de Reajuste Salarial".
# 2. Pedir ao usuário:
#    - nome do funcionário
#    - salário atual
#    - quantidade de dependentes

# Depois disso, o programa deve calcular o aumento do salário
# de acordo com as seguintes regras:

# Se o funcionário NÃO tiver dependentes:
# aumento de 5% no salário.

# Se tiver de 1 a 3 dependentes:
# aumento de 10% no salário.

# Se tiver de 4 a 5 dependentes:
# aumento de 15% no salário.

# O programa deve mostrar:

# nome do funcionário
# salário atual
# quantidade de dependentes
# novo salário após o aumento

print("Sistema de Reajuste Salarial")

# Pedido de dados
nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário atual: "))
dependentes = int(input("Digite a quantidade de dependentes: "))

# Verificando a porcentagem de aumento
# Calculo de porcentagem Ex: (Salario *5/100) (Salario *10/100)

if dependentes == 0:
    aumento = 0.05 #5%
elif dependentes >= 1 and dependentes <= 3:
    aumento = 0.10 #10%
elif dependentes >= 4 and dependentes <= 5:
    aumento = 0.15 #15%
else:
    aumento = 15 #caso tenha mais de 5 dependentes

# Calculando o novo salário
novo_salario = salario * (1 + aumento/100)      

# Mostrando resultado
print("\n--- Resultado ---")
print(f"Nome do funcionário: {nome}")
print(f"Salário atual: R$ {salario:.2f}")
print(f"Quantidade de dependentes: {dependentes}")
print(f"Novo salário: R$ {novo_salario:.2f}")