# Operadore aritméticos no Python

# + -> Adição

# - -> Subtração

# * -> Multiplicação

# / -> Divisão

# // -> Divisão inteira (retorna o quociente sem a parte decimal) O modulo é útil quando você precisa do resultado como um número inteiro, 
# descartando a parte decimal. Por exemplo, 10 // 3 resulta em 3.  
# Mesmo que o resultado da divisão seja um número decimal, a divisão inteira sempre retorna um número inteiro.

# % -> Módulo (retorna o resto da divisão) O modulo é útil para verificar se um número é par ou ímpar, por exemplo. Se a saida de 
# num % 2 for 0, o número é par; se for 1, o número é ímpar.

# ** -> Exponenciação (potenciação) O modulo é útil para calcular potências, como 2 elevado a 3 (2 ** 3), que resulta em 8.

print("Operadores Aritmeticos")
print("Adicao: ", 10 + 5)          # Saída: 15
print("Subtracao: ", 10 - 5)       # Saída: 5
print("Multiplicacao: ", 10 * 5)    # Saída: 50
print("Divisao: ", 10 / 5)         # Saída: 2.0
print("Divisao Inteira: ", 10 // 3) # Saída: 3
print("Módulo: ", 10 % 3)          # Saída : 1
print("Exponenciacao: ", 2 ** 3)    # Saída: 8

# Ordem de precedência dos operadores
# 1. Parênteses ()
# 2. Exponenciação ** 
# 3. Multiplicação * , Divisão / , Divisão Inteira // , Módulo %
# 4. Adição + , Subtração -


print("Ordem de Precedencia")
resultado = 10 + 5 * 2 ** 2  # Equivale a 10 + 5 * 4 = 10 + 20 = 30 


print("Resultado sem parenteses: ", resultado)  # Saída: 30

resultado_com_parenteses = (10 + 5) * 2 ** 2  # Equivale a 15 * 4 = 60

print("Resultado com parenteses: ", resultado_com_parenteses)  # Saída: 60

# Você pode usar parênteses para alterar a ordem de avaliação das expressões
# Exemplo:

expressao = (10 - 2) * (5 + 3) / 4  # Equivale a 8 * 8 / 4 = 64 / 4 = 16.0

print("Expressao com parenteses: ", expressao)  # Saída: 16.0

print("----------------")
