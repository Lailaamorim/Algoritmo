# =========================================
# DESAFIO 07
# Peça quanto dinheiro a pessoa tem na carteira
# e converta para dólares (considere 1 dólar = 5 reais).
#
# SAÍDA ESPERADA:
# Você pode comprar 20.0 dólares
# =========================================
num = float(input("Quanto R$ você tem na carteira? "))
print(f"Você tem R${num}\nVocê pode comprar US${num/5.15:.2f}")