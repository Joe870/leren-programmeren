# name of student: Joëlle van Breugel
# number of student: 99075308
# purpose of program: 
# function of program:
# structure of program: 
change_zin=''
change_value=''

toPay = int(float(input('Amount to pay: '))* 100) #je vraagt hoeveel iemand moet betalen dan maak je er een float van en dan maak je er een integer getal van
paid = int(float(input('Paid amount: ')) * 100) #je vraagt hoeveel iemand heeft betaald dan maak je er een float van en dan maak je er een integer getal van
change = paid - toPay #dit is som waarbij je topay - paid doet. 

if change > 0: #als de som groter dan 0 is
  coinValue = 500 #dan is de waarde van de munten 50 
  
  while change > 0 and coinValue > 0: #als de som groter dan 0 is en de coinvalue groter dan 50
    nrCoins = change // coinValue #deel je de som door de coinvalue 

    if nrCoins > 0: #als de gedeelde som groter dan 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #nrcoins is de gedeelde som en coinvalue = 50 of 0 
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #je vraagt hoeveel munten van de bepaalde coinvalue je terug hebt gegeven
      change -= nrCoinsReturned * coinValue #nieuw wisselgeld is de input van regel 19 keer coinvalue
      change_zin += f'{nrCoinsReturned} coins of {coinValue}\n'


      

# comment on code below: 
# dit zorgt ervoor dat de munten de juiste waarde krijgen.
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2 
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0
print(change_zin)   
if change > 0: #als change groter dan nul is print regel 37 ander print regel 39
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')