import random

"""
1 - choice() 
Funcionalidade: Retorna um elemento aleatório de uma sequência não vazia
"""
choiceNumbersRandom = [7, 6, 4,  3, 2, 1]
choiceTextRandom = "Python-Course"
print(random.choice(choiceNumbersRandom))
print(random.choice(choiceTextRandom))

"""
2 - radiant()
Funcionalidade: Retorna um número inteiro aleatório no intervalo fechado
"""
radiantRandom = random.randint(10, 50)
print(radiantRandom)

"""
3 - uniform()
uncionalidade: Retorna um número float aleatório no intervalo 
"""
floatRandom = random.uniform(10.8, 28.9)
print(floatRandom)

"""
4 - shuffle()
Funcionalidade: Embaralha aleatoriamente os elementos de uma sequência
"""
shuffleNumber = [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', '@', '/']
random.shuffle(shuffleNumber)
print(shuffleNumber)

"""
5 - sample()
Funcionalidade: Retorna uma lista de elementos aleatórios únicos de uma variável, array, ect....
"""
supleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.sample(supleList, 4))