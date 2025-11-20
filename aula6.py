# Conversão de tipos , coercão de tipos
# Em Python, é possível converter um tipo de dado em outro usando funções de conversão embutidas.
# As funções mais comuns para conversão de tipos são:   
# int() -> Converte um valor para o tipo inteiro
# float() -> Converte um valor para o tipo float (ponto flutuante)
# str() -> Converte um valor para o tipo string (texto)

print("Conversão de tipos")
# Convertendo string para inteiro
num_str = "100" 
num_int = int(num_str)
print(num_int)          # Saída: 100

# Convertendo string para float
num_str_float = "10.5"
num_float = float(num_str_float)
print(num_float)        # Saída: 10.5

# Convertendo inteiro para string
num_int2 = 200
num_str2 = str(num_int2)
print(num_str2)         # Saída: "200"

# Convertendo float para inteiro
num_float2 = 9.99   
num_int3 = int(num_float2)
print(num_int3)        # Saída: 9 (parte decimal é truncada)    


# Convertendo inteiro para float
num_int4 = 7
num_float3 = float(num_int4)
print(num_float3)      # Saída: 7.0

# Coerção de tipos
# Em expressões que envolvem múltiplos tipos de dados, o Python realiza a coerção automática de tipos quando necessário.
# Por exemplo, ao somar um inteiro e um float, o Python converte o inteiro para float antes de realizar a operação.

int_value = 5
float_value = 2.5
result = int_value + float_value  # int é convertido para float
print(result)  # Saída: 7.5
print(type(result))  # Saída: <class 'float'>

# Ao concatenar uma string com um número, é necessário converter o número para string explicitamente.
str_value = "O número é: " + str(int_value) 
print(str_value)  # Saída: "O número é: 5"

# Tentativa de concatenar string com número sem conversão resulta em erro
# str_value_error = "O número é: " + int_value  # Isso causará um TypeError     