# Variaveis são usadas para armazenar valores na memória

# PEP 8 - Guia de estilo para Python 

# Inicie sempre as variáveis com letras minúsculas ou underscore (_)

# Nomes de variáveis podem conter letras, números e underscores (_)

# Exemplos de nomes de variáveis válidos: idade, nome_usuario, _contador, valor2

# O sinal de igual (=) é usado para atribuir valores às variáveis
# Uso: nome_variavel = valor

idade = 25  # Atribui o valor 25 à variável idade
nome_usuario = "Daniel"  # Atribui a string "Daniel" à variável nome_usuario
_contador = 10  # Atribui o valor 10 à variável _contador
valor2 = 15.5  # Atribui o valor 15.5 à variável valor2
print(idade)  # Imprime o valor da variável idade
print(nome_usuario)  # Imprime o valor da variável nome_usuario
print(_contador)  # Imprime o valor da variável _contador
print(valor2)  # Imprime o valor da variável valor2

# Evite usar palavras reservadas do Python como nomes de variáveis
# Exemplo de palavra reservada: def, class, if, else, return, etc.

# Exemplo incorreto:
# def = 10  # Isso causará um erro, pois "def" é uma palavra reservada

# Exemplo correto:
definicao = 10  # Isso é válido, pois "definicao" não é uma palavra reservada
print(definicao)  # Imprime o valor da variável definicao

# Boa prática: Use nomes de variáveis descritivos para melhorar a legibilidade do código
# Exemplo:

numero_de_alunos = 30  # Melhor do que apenas "n" ou "x"
print(numero_de_alunos)  # Imprime o valor da variável numero_de_alunos 



# Evite usar caracteres especiais ou espaços em nomes de variáveis

# Exemplo incorreto:    

# nome usuario = "Ana"  # Isso causará um erro devido ao espaço

# Exemplo incorreto:

# nome-usuario = "Ana"  # Isso causará um erro devido ao caractere especial "-"

# Exemplo correto:
nome_usuario = "Ana"  # Isso é válido


