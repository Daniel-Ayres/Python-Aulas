# Introdução a formatação de strings com f-strings

print("Formatacao de Strings com f-strings")
nome = "Alice"
idade = 30
altura = 1.65
imc = 22.04
# Usando f-strings para formatar a saída
print(f"Nome: {nome}, Idade: {idade} anos, Altura: {altura} m, IMC: {imc}")  # Saída: Nome: Alice, Idade: 30 anos, Altura: 1.65 m, IMC: 22.04

# Formatação avançada com f-strings
print("Formatacao Avancada com f-strings")
pi = 3.141592653589793
print(f"Valor de pi com 2 casas decimais: {pi:.2f}")  # Saída: Valor de pi com 2 casas decimais: 3.14
print(f"Valor de pi com 5 casas decimais: {pi:.5f}")  # Saída: Valor de pi com 5 casas decimais: 3.14159
print(f"Valor de pi em notacao cientifica: {pi:.2e}")  # Saída: Valor de pi em notacao cientifica: 3.14e+00
print(f"Valor de pi com preenchimento e alinhamento: {pi:10.2f}")  # Saída: Valor de pi com preenchimento e alinhamento:       3.14
print("----------------")

# A formatoção de strings com f-strings é uma maneira poderosa e flexível de incorporar expressões dentro de strings literais,
# permitindo uma apresentação clara e personalizada dos dados.
