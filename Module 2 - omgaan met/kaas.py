kaas = input('is de kaas geel:')
if kaas == 'ja':
    gaten = input('zitten er gaten in?') 
    if gaten == 'ja':
        duur = input('is de kaas belachelijk duur?')
        if duur == 'ja':
            print('emmentaler')
        else: print('leerdammer') 
    else:
        hard = input('is de kaas hard als steen?') 
        if hard == 'ja':
            print('parmigiano reggianno')
        else: print('goudse kaas')
else:
    schimmel = input('heeft de kaas blauwe schimmel?')
    if schimmel == 'ja': 
        korst = input('heeft de kaas een korst?')
        if korst == 'ja':
            print('blue de rochbaron')
        else: print('foume d ambert') 
    else:
        korst = input('heeft de kaas een korst?') 
        if korst == 'ja': 
            stank = input('stinkt de kaas')
            if stank == 'ja':
                print('camembert') 
            else: print('brie') 
         
        
        else: print('mozzarella') 


    

    


