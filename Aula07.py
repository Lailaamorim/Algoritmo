# ---------------------------------------------------
# AULA BÁSICA - FUNÇÕES (ROTINAS) EM PYTHON
# ---------------------------------------------------

# Em Python usamos FUNÇÕES para:
# - organizar o código
# - evitar repetir código
# - dividir o programa em partes menores
# - reutilizar código várias vezes

# No Visualg existem:
# procedimento -> não retorna valor
# função -> retorna valor

# Em Python os dois são feitos com:
# def

# def significa: definir uma função


# ---------------------------------------------------
# ESTRUTURA BÁSICA DE UMA FUNÇÃO
# ---------------------------------------------------

# def -> cria a função
# nome_funcao -> nome que você escolhe
# () -> parâmetros (valores que podem entrar na função)
# : -> início do bloco da função

def mostrar_mensagem():
    print("Olá mundo")


# chamando (executando) a função
mostrar_mensagem()


# ---------------------------------------------------
# FUNÇÃO SEM PARÂMETROS
# ---------------------------------------------------

# essa função apenas executa algo

def saudacao():
    print("Bem-vindo ao sistema!")

saudacao()


# ---------------------------------------------------
# FUNÇÃO COM PARÂMETROS
# ---------------------------------------------------

# parâmetros são valores que entram na função

def soma(a, b):
    resultado = a + b
    print("Resultado:", resultado)

# chamando a função e passando valores
soma(5, 3)


# ---------------------------------------------------
# FUNÇÃO COM RETORNO (RETURN)
# ---------------------------------------------------

# return faz a função devolver um valor

def somar(a, b):
    return a + b

resultado = somar(10, 5)

print("Resultado:", resultado)


# ---------------------------------------------------
# EXEMPLO PRÁTICO
# ---------------------------------------------------

# função que calcula média

def calcular_media(n1, n2):

    media = (n1 + n2) / 2

    return media


# entrada de dados
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

# usando a função
media_final = calcular_media(nota1, nota2)

print("Média:", media_final)


# ---------------------------------------------------
# OUTRO EXEMPLO - VERIFICAR IDADE
# ---------------------------------------------------

def verificar_idade(idade):

    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")


idade_usuario = int(input("Digite sua idade: "))

verificar_idade(idade_usuario)


# ---------------------------------------------------
# REGRAS IMPORTANTES
# ---------------------------------------------------

# 1 - A função precisa ser criada antes de ser usada

# errado
# somar()
# def somar():
#     print("Olá")

# certo
# def somar():
#     print("Olá")
# somar()


# 2 - Python usa indentação (espaços) para organizar blocos

# exemplo

idade = 20

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


# ---------------------------------------------------
# RESUMO
# ---------------------------------------------------

# def -> cria função
# () -> parâmetros
# return -> retorna valor
# função -> organiza e reutiliza código