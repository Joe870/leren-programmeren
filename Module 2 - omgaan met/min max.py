A = input('A=') 
B = input('B=')
if A > B: 
    max = A
    min = B
    print(f'A is het grootste getal: {max}') 
elif B > A:
    max = B
    min = A 
    print(f'A is het kleinste getal: {min}') 
else: print('A en B zijn even groot')
print(f'het maximum is {max}')
print(f'het minimum is {min}') 