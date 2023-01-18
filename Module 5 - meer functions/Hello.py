def hellopython(y):
    zin = ''
    for x in range(1, y + 1): 
        zin += f"hello from function town! {x}\n"
    return zin

userInput = int(input("Hoeveel?"))
print(hellopython(userInput))