# =========================================
# DESAFIO 09 - VALIDADOR DE SENHA FORTE
#
# Peça ao usuário para digitar uma senha.
#
# O programa deve verificar se a senha é forte.
#
# REGRAS PARA SER UMA SENHA FORTE:
# - Deve ter pelo menos 8 caracteres
# - Deve ter pelo menos 1 número
# - Deve ter pelo menos 1 letra maiúscula
#
# MOSTRAR:
# "Senha forte"
# ou
# "Senha fraca"
#
# =========================================
# =========================================
# DESAFIO 09 - VALIDADOR DE SENHA FORTE
# =========================================

# Pede para o usuário digitar uma senha
senha = input("Digite sua senha: ")

# Variáveis para verificar as condições
tem_numero = False        # Vai verificar se tem número
tem_maiuscula = False     # Vai verificar se tem letra maiúscula

# Percorre cada caractere da senha
for c in senha:
    # Verifica se o caractere é um número
    if c.isdigit():
        tem_numero = True
    
    # Verifica se o caractere é uma letra maiúscula
    if c.isupper():
        tem_maiuscula = True

# Verifica todas as condições:
# - Pelo menos 8 caracteres
# - Tem número
# - Tem letra maiúscula
if len(senha) >= 8 and tem_numero and tem_maiuscula:
    print("Senha forte")
else:
    print("Senha fraca")       
