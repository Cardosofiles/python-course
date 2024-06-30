from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista 
fruits = ['Maça', 'Banana', 'Uva', 'Melancia', 'Maça', 'Uva', 'Pera', 'Abacaxi', 'Melancia', 'Uva']
print(fruits)
print(Counter(fruits))

# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game('Fifa23', 90.50, 8.5)
g2 = game('Resident Evil 4 Remake', 300, 10.0)
print(g1)
print(g2)

# 3 - Ordenando dicionários
studants = {'Pedro':23, 'Ana':22, 'Ronaldo':26, 'Janaína':25}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)

# 4 - Utilizando fila ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
deq.append(90)
deq.popleft()
deq.pop()
print(deq)