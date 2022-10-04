kaas = input('is de kaas geel:')
if kaas == 'ja':
    gaten = input('zitten er gaten in?') 
    if gaten == 'ja':
        duur = input('is de kaas belachelijk duur?')
        if duur == 'ja':
            print('emmentaler')
        elif duur == 'nee':
            print('leerdammer') 
    elif gaten == 'nee':
        hard = input('is de kaas hard als steen?') 
        if hard == 'ja':
            print('parmigiano reggianno')
        elif hard == 'nee':
            print('goudse kaas')
elif kaas == 'nee': 
    schimmel = input('heeft de kaas blauwe schimmel?')
    if schimmel == 'ja': 
        korst = input('heeft de kaas een korst?')
        if korst == 'ja':
            print('blue de rochbaron')
        elif korst == 'nee': 
            print('foume d ambert') 
    elif schimmel == 'nee': 
        korst = input('heeft de kaas een korst?') 
        if korst == 'ja':
            print('camembert')
        elif korst == 'nee':
            print('mozzarella') 


    

    


