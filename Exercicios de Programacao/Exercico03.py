# --- CÁLCULO DE IMC ---

# 1. Entrada de dados
# Usamos float() porque peso e altura podem ter números decimais (ex: 1.75)
peso = float(input("Digite seu peso em kg (ex: 70): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

# 2. Processamento: Cálculo do IMC
# A fórmula é peso dividido pela altura ao quadrado (altura ** 2)
imc = peso / (altura ** 2)

# 3. Exibição do valor formatado
print(f"\nSeu IMC é: {imc:.2f}")

# 4. Lógica de Classificação (Tomada de Decisão)
if imc < 17:
    print("Classificação: Muito abaixo do peso.")
elif 17 <= imc < 18.5:
    print("Classificação: Abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Classificação: Peso ideal (parabéns!).")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso.")
elif 30 <= imc < 35:
    print("Classificação: Obesidade.")
elif 35 <= imc < 40:
    print("Classificação: Obesidade severa.")
else:
    print("Classificação: Obesidade mórbida.")