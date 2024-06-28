import math

# 1 - Accessing the number PI
print("Número PI")
print(math.pi)
print(f"{math.pi:.2f}")

# 2 - Accessing the number Euler
print("Número Euler")
print(math.e)
print(f"{math.e:.2f}")

# 3 - Method of rounding numbers up and down
print("Método de arrendondamento de um número para cima e para baixo")
num = 10.4
print(math.ceil(num))
print(math.floor(num))

# 4 - Factorial of a number
print("Método de arrendondamento de um número")
num = int(input("Digite um número para o fatorial:\n"))
print (math.factorial(num))

# 5 - Power of a number
print("Método Potência de números")
print(math.pow(5,5))

# 6 - Square root
print("Método Raiz quadrada")
print(math.sqrt(169))

# 7 - MDC
print("Maior divisor comum")
mdc = math.gcd(25, 100)
print(mdc)

# 8 - Logaritmo
print(math.log(10))