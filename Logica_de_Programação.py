"""
================================================================================
GUIA COMPLETO DE LÓGICA DE PROGRAMAÇÃO E PYTHON
================================================================================

1. O QUE É UM ALGORITMO? (A LÓGICA DO BOLO)
Um algoritmo é uma sequência lógica de passos para resolver um problema.
Exemplo: Fazer um café.
- PASSO 1: Colocar água na cafeteira.
- PASSO 2: Colocar o pó de café.
- PASSO 3: Ligar a cafeteira.
- PASSO 4: Servir na xícara.
Na programação, se você inverter a ordem (ex: servir antes de colocar água), 
o código falha ou gera um resultado inesperado.

================================================================================
2. VARIÁVEIS E TIPOS DE DADOS
Variáveis são "caixas" na memória do computador.
"""
nome = "Maria"          # str (Texto)
idade = 25              # int (Inteiro)
altura = 1.75           # float (Decimal)
esta_estudando = True   # bool (Booleano: True/False)

# 3. ENTRADA E SAÍDA DE DADOS
# print() mostra na tela, input() recebe do usuário.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"Olá {nome}, você tem {idade} anos.")

# 4. OPERADORES ARITMÉTICOS
a = 10
b = 3
print(a + b)  # Soma (13)
print(a - b)  # Subtração (7)
print(a * b)  # Multiplicação (30)
print(a / b)  # Divisão real (3.333...)
print(a // b) # Divisão inteira (3)
print(a % b)  # Resto da divisão (1)
print(a ** b) # Exponenciação (1000)

# 5. OPERADORES DE COMPARAÇÃO (RELACIONAIS)
# Usados para comparar dois valores. Retornam True ou False.
x = 10
y = 5

print(x > y)   # Maior que (True)
print(x < y)   # Menor que (False)
print(x >= y)  # Maior ou igual a (True)
print(x <= y)  # Menor ou igual a (False)
print(x == y)  # Igual a (compara valor) (False)
print(x != y)  # Diferente de (True)
# AVISO: Um único sinal de igual (=) é ATRIBUIÇÃO (guarda valor), 
# dois sinais (==) é COMPARAÇÃO.

# 6. OPERADORES LÓGICOS
# Combinam condições.
print(x > 5 and y < 10) # AND (E): Ambos precisam ser verdadeiros (True)
print(x > 5 or y > 20)  # OR (OU): Pelo menos um precisa ser verdadeiro (True)
print(not (x == y))     # NOT (NÃO): Inverte o resultado (True vira False)

# 7. ESTRUTURAS CONDICIONAIS (IF, ELIF, ELSE)
# Decidem qual caminho o código deve seguir.
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 13:
    print("Você é um adolescente.")
else:
    print("Você é uma criança.")

# 8. ESTRUTURAS DE REPETIÇÃO (LOOPS)
# FOR: Usado quando sabemos quantas vezes repetir ou para percorrer algo.
print("Contagem com FOR:")
for i in range(3): # Repete 0, 1, 2
    print(f"Passo {i}")

# WHILE: Usado para repetir enquanto uma condição for verdadeira.
contador = 0
print("Contagem com WHILE:")
while contador < 3:
    print(f"Contador: {contador}")
    contador = contador + 1

# 9. LISTAS (Coleções de dados)
frutas = ["Maçã", "Banana", "Uva"]
print(frutas[0])        # Acessar o primeiro item (Índice 0)
frutas.append("Manga")  # Adicionar item
print(f"Lista completa: {frutas}")

# 10. DICIONÁRIOS (Dados complexos com chave e valor)
pessoa = {
    "nome": "João",
    "idade": 30
}
print(f"Nome do usuário: {pessoa['nome']}")

# 11. FUNÇÕES (Blocos de código reutilizáveis)
def somar(n1, n2):
    return n1 + n2

resultado_funcao = somar(10, 5)
print(f"Resultado da função: {resultado_funcao}")

# 12. ORDEM DE PRECEDÊNCIA (Quem manda primeiro)
"""
1º () Parênteses
2º ** Exponenciação
3º *, /, //, % Multiplicação e Divisão
4º +, - Adição e Subtração
5º >, <, >=, <=, ==, != Comparadores
6º not, and, or Operadores Lógicos
"""