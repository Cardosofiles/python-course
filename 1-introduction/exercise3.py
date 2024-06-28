distance = float(input("Digite a distância a percorrer: "))
if distance <= 200:
    ticket = 0.5 * distance
else:
    ticket = 0.35 * distance
print(f"Preço da passagem: R$ {ticket:.2f}")

salary = float(input("Digite seu salário: "))
perc_increase = 0.15
if salary > 1250:
    perc_increase = 0.10
incresase = salary * perc_increase
print(f"Seu aumento será de: R$ {incresase:.2f}")