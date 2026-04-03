# EXERCÍCIO 10 - CADASTRO DE PESSOAS

# criar um programa para cadastrar várias pessoas

# perguntar o sexo da pessoa (masculino ou feminino)

# perguntar a idade da pessoa

# perguntar a cor da pele
# 1 branca
# 2 parda
# 3 preta
# 4 amarela
# 5 indígena

# perguntar a cor dos olhos
# 1 castanho
# 2 azul
# 3 verde
# 4 preto
# 5 mel

# perguntar a cor do cabelo
# 1 preto
# 2 castanho
# 3 loiro
# 4 ruivo

# perguntar o tamanho da roupa
# P
# M
# G
# GG

# perguntar a profissão
# 1 professor
# 2 médico
# 3 engenheiro
# 4 programador
# 5 designer
# 6 enfermeiro
# 7 policial
# 8 mecânico
# 9 motorista
# 10 estudante

# perguntar se deseja continuar cadastrando pessoas

# repetir o cadastro enquanto o usuário quiser continuar

# no final mostrar resultados com base nas características cadastradas

print("-"*30)
print("CADASTRO DE PESSOAS")
print("-"*30)

# Contadores
homens_18 = 0
mulheres_loiras = 0

continuar = "s"

while continuar == "s":

    sexo = input("Sexo (M/F): ").lower()
    idade = int(input("Idade: "))

    # Cor da pele
    print("\nCor da pele:")
    print("1 - Branca")
    print("2 - Parda")
    print("3 - Preta")
    print("4 - Amarela")
    print("5 - Indígena")
    pele = int(input("Escolha: "))

    # Cor dos olhos
    print("\nCor dos olhos:")
    print("1 - Castanho")
    print("2 - Azul")
    print("3 - Verde")
    print("4 - Preto")
    print("5 - Mel")
    olhos = int(input("Escolha: "))

    # Cor do cabelo
    print("\nCor do cabelo:")
    print("1 - Preto")
    print("2 - Castanho")
    print("3 - Loiro")
    print("4 - Ruivo")
    cabelo = int(input("Escolha: "))

    # Tamanho da roupa
    tamanho = input("\nTamanho de roupa (P/M/G/GG): ").upper()

    # Profissão
    print("\nProfissão:")
    print("1 - Professor")
    print("2 - Médico")
    print("3 - Engenheiro")
    print("4 - Programador")
    print("5 - Designer")
    print("6 - Enfermeiro")
    print("7 - Policial")
    print("8 - Mecânico")
    print("9 - Motorista")
    print("10 - Estudante")
    profissao = int(input("Escolha: "))

    # Homens maiores de 18
    if sexo == "m" and idade > 18:
        homens_18 += 1

    # Mulheres entre 25 e 30 com cabelo loiro
    if sexo == "f" and 25 <= idade <= 30 and cabelo == 3:
        mulheres_loiras += 1

    # Pergunta se deseja continuar
    continuar = input("\nDeseja continuar cadastrando? (s/n): ").lower()


# Resultados finais (fora do while)
print("\n" + "-"*30)
print("RESULTADOS")
print("-"*30)

print(f"Homens com mais de 18 anos: {homens_18}")
print(f"Mulheres entre 25 e 30 anos com cabelo loiro: {mulheres_loiras}")