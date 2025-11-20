# Tipo de dados booleano
# bool -> Valores booleanos (True ou False)
# So existem dois valores booleanos em Python: True (verdadeiro) e False (falso).
# Existem varios operadores para questiorar valores booleanos, como os operadores de comparação e os operadores lógicos.
# Dentro eles o == , que um operador de comparação que verifica se dois valores são iguais.
print("Tipos BOOL")
print(True)   # Saída: True
print(False)  # Saída: False
print(type(True))   # Saída: <class 'bool'>
print(type(False))  # Saída: <class 'bool'>

print(10 == 10)  # Saída: True
print(10 == 5)   # Saída: False

print("----------------")

print(5 > 3, 'Cinco maior que tres?')    # Maior que R: True
print(5 < 10, 'Cinco menor que dez?')   # Menor que R: True
print(5 < 3, 'Cinco menor que tres?')    # Menor que R: False
print(5 >= 5, 'Cinco maior ou igual a cinco?')   # Maior ou igual a R: True
print(5 <= 2, 'Cinco menor ou igual a dois?')   # Menor ou igual a R: False
print(5 != 2, 'Cinco diferente de dois?')   # Diferente de R: True
print(5 != 5, 'Cinco diferente de cinco?')   # Diferente de R: False
print("----------------")