import webbrowser

done = False

while not done: 
  print("O que deseja fazer?")
  print("1. Aprender Python?")
  print("2. Aprender JavaScript?")
  print("3. Aprender React>")
  print("4. Sair")

  choice = input(">")
  
  if choice == "1":
    webbrowser.open("https://www.w3schools.com/python/default.asp")
  
  elif choice == "2":
    webbrowser.open("https://www.w3schools.com/js/default.asp")
  
  elif choice == "3":
    webbrowser.open("https://www.w3schools.com/react/default.asp")
  
  elif choice == "4":
    done = True
    
  else: 
    print("Opção inválida. Escolha uma opção válida")