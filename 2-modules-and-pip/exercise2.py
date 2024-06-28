import os  # Importa o módulo os, que permite a execução de comandos do sistema operacional

# Desligar o computador em 1 minuto
os.system('shutdown /s /t 60')

# Cancelar o desligamento
os.system('shutdown /a')

def turn_off_one_hour():
  """
  Esta função agenda o desligamento do computador em 1 hora (3600 segundos).
  """
  os.system('shutdown /s /t 3600')

def turn_off_half_an_hour():
  """
  Esta função agenda o desligamento do computador em meia hora (1800 segundos).
  """
  os.system('shutdown /s /t 1800')

def cancel_shutdown():
  """
  Esta função cancela qualquer desligamento agendado.
  """
  os.system('shutdown /a')

# Agenda o desligamento do computador em 1 hora
turn_off_one_hour()

# Cancela o desligamento agendado anteriormente
cancel_shutdown()

# Agenda o desligamento do computador em meia hora
turn_off_half_an_hour()

# Cancela o desligamento agendado anteriormente
cancel_shutdown()
