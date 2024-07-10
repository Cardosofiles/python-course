"""
### Files:
1 - option w - write
2 - option a - append
3 - option r - read
"""

# Opção 01, arquivo em mesma pasta
with open ("reading.txt", "r") as file :
  for line in file:
    print(line)

# Opçaõ 02, arquivo fora da pasta pai do "name".py
with open ("../db/text.txt", "r") as file :
  for line in file:
    print(line)

# Opção 02.1, método .rstrip() remove linhas em branco
with open ("../db/text.txt", "r") as file :
  for line in file:
    print(f"{line.rstrip()}") # f"{}" para utilizar string com conteúdo do arquivo

# Opção 02.3, método encoding=(), valida caracteres especiais
with open ("../db/text.txt", "r", encoding="utf-8") as file : 
  for line in file:
    print(line.rstrip())