name = input("Digite o seu nome:\n")

"""
### Files:
1 - option w - write
2 - option a - append
3 - option r - read
"""

"""
# Alternativa 01
file = open("writing.txt", "a")
file.write(f"{name}\n")
file.close()
"""
# Alternativa 02
with open("writing.txt", "a") as file: 
  file.write(f"{name}\n")


