vraag_tafel= int(input('van welk getal wil je een tafel zien'))

def print_tafel(basis):
    uitkomst = ""
    for getal in range(1, 11):
        uitkomst += f'{getal} * {basis} = {getal * basis}\n'
    return uitkomst

print(print_tafel(vraag_tafel))


