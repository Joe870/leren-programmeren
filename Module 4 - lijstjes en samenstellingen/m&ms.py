tuple = ("oranje", "blauw", "groen", "bruin")
aantal_mms = input('hoeveel m&ms moeten er aan de zak worden toegevoegd?')
list = [] 
list.append(aantal_mms)
print(list)
list.extend(tuple)
print(list)