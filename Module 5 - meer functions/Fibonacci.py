def fibonacci_next(fibo_lijst: list) -> list:
    som_toevoeg=int(fibo_lijst[-1]) + int(fibo_lijst[-2])
    fibo_lijst.append(som_toevoeg)
    return fibo_lijst
hoe_vaak = int(input('hoe veel getallen wil je toevoegen'))
def reeks_fibonacci(limit:int) ->list:
    reeks = [0,1]
    for x in range(limit):
        reeks=fibonacci_next(reeks)
    return reeks
uitkomst_toevoeg = reeks_fibonacci(hoe_vaak)
print(uitkomst_toevoeg)

def gulden_snede(getal:int) ->list:
    som_snede = int(uitkomst_toevoeg[-1]) / int(uitkomst_toevoeg[-2])
    return som_snede
uitkomst=gulden_snede(uitkomst_toevoeg)
print(uitkomst)