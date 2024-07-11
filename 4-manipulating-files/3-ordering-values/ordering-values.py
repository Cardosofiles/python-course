# Cria uma lista vazia para armazenar os nomes lidos do arquivo
names = []

# Abre o arquivo "names.txt" localizado no diretório db da pasta atual e lê seu conteúdo
# O arquivo é aberto no modo de leitura ("r") e com codificação "utf-8"
with open("../db/names.txt", "r", encoding="utf-8") as file:
  # Itera sobre cada linha do arquivo
  for line in file:
    """Remove espaços em branco e valida os caracteres especiais e volta uma
    nova linha do final de cada linha e adiciona a linha à lista "names". """
    names.append(line.rstrip())

# Ordena a lista de nomes em ordem alfabética
for name in sorted(names):
  # Imprime cada nome na lista ordenada
  print(name)
