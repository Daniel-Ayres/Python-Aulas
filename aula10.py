# Concatenação e repetição com operadores aritméticos
print("Concatenacao e Repeticao")
# Concatenação de strings usando o operador +
str1 = "Ola, "
str2 = "mundo!"
concatenacao = str1 + str2
print("Concatenacao: ", concatenacao)  # Saída: Olá, mundo!

# Repetição de strings usando o operador *
str3 = "Python! "
repeticao = str3 * 3
print("Repeticao: ", repeticao)  # Saída: Python! Python! Python!
print("----------------")

# Mistura de tipos com operadores aritméticos
print("Mistura de Tipos")
# Adição de número e string (necessário converter o número para string)
num = 10
texto = " e um numero."
resultado_adicao = str(num) + texto
print("Adicao (numero + string): ", resultado_adicao)  # Saída: 10 é um número.

# Multiplicação de string e número (necessário converter o número para inteiro)
str4 = "Repetir! "
num_repeticoes = 4
resultado_multiplicacao = str4 * int(num_repeticoes)
print("Multiplicacao (string * numero): ", resultado_multiplicacao)  # Saída: Repetir! Repetir! Repetir! Repetir!
print("----------------")