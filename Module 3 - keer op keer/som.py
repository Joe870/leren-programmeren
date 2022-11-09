cijfer_1 = 50
som = 0
som_text = ''
while cijfer_1 <100 and som<1000:
    print(cijfer_1)
    cijfer_1 = cijfer_1 + 1
    print(cijfer_1)
    som += cijfer_1
    som_text += str(f'{cijfer_1}+')
    print(f'{som_text} = {som}')

