from fruitmand import fruitmand
for index in range(len(fruitmand)):
    if fruitmand[index]['name'] == 'druif':
        fruitmand.pop(index)
print(fruitmand)
for fruit in fruitmand:
    print(fruit['color'])