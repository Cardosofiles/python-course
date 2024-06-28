teams = {} 
done = False
while not done:
  # print options
  print("O que você deseja fazer?")
  print("1. Adicionar um time")
  print("2. Remover um time")
  print("3. Listar times")
  print("4. Adicionar jogador em um time")
  print("5. Remover jogador em um time")
  print("6. Listar jogadores de um time")
  print("7. Sair")
  
  # get user input
  choice = input("> ")

  if choice == "1":
    pass
  elif choice == "2":
    pass
  elif choice == "3":
    pass
  elif choice == "4":
    pass
  elif choice == "5":
    pass
  elif choice == "6":
    pass
  elif choice == "7":
    feito = True
  else:
    print("Opção inválida")
	# função para listar times
   
def print_teams():
  print("Times listados:")
  for i, team in enumerate(teams.values()):
    print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")

# função para listar jogadores de um time
def print_team_players(team):
  print(f"Jogadores do {team['name']}:")
  for i, player in enumerate(team['players']):
    print(f"{i+1}. {player}")

# Adiciona um time
if choice == "1":
  team_name = input("Digite o nome do time: ")
  teams[team_name] = {'name': team_name, 'players': []}
  print("Time adicionado.")
        
# Remove um time
elif choice == "2":
  print_teams()
  team_num = int(input("Informe o número do time para remover: "))
  if team_num <= len(teams):
    team_name = list(teams.keys())[team_num-1]
    del teams[team_name]
    print("Time removido.")
  else:
    print("Número de time inválido.")

# Lista times
elif choice == "3":
  print_teams()

# Adicionar jogador em um time
elif choice == "4":
  print_teams()
  team_num = int(input("Informe o número do time que deseja adicionar jogador: "))
  if team_num <= len(teams):
    team_name = list(teams.keys())[team_num-1]
    player_name = input("Informe o nome do jogador: ")
    teams[team_name]['players'].append(player_name)
    print("Jogador adicionado no time.")
  else:
    print("Número do time inválido")
    
    # Remove jogador de um time
elif choice == "5":
  print_teams()
  team_num = int(input("Informe o número do time que deseja adicionar jogador: "))
  if team_num <= len(teams):
    team_name = list(teams.keys())[team_num-1]
    print_team_players(teams[team_name])
    player_num = int(input("Informe o número do jogador para remover: "))
    if player_num <= len(teams[team_name]['players']):
        del teams[team_name]['players'][player_num-1]
        print("Jogador removido do time.")
    else:
        print("Número do jogador inválido.")
  else:
    print("Número do time inválido.")
    
    # Lista jogadores de um time
elif choice == "6":
  print_teams()
  team_num = int(input("Informe o número do time para listar jogadores: "))
  if team_num <= len(teams):
    team_name = list(teams.keys())[team_num-1]
    print_team_players(teams[team_name])
  else:
    print("Número do time inválido.")

# exit
elif choice == "7":
  done = True

# invalid choice
else:
  print("Opção inválida.")