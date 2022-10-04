print('speeltuin entree')

# welkom voor kinderen van 12 of onder de 12, maar alleen met een begeleider van 20 of ouder
# of welkom als ze onder de 14 zijn en een speeltuinpasje hebben
# of welkom als ze een begeleider hebben met de naam Vladimir 

age = 20
pasje = 'ja'
begeleider = 'ja'
age_begeleider = 20
naam_begeleider = 'Joseph'

if "age <= 12": 
  print('Je mag naar binnen')

if "age > 12":
  print('sorry, alleen voor de jonge kinderen')

if bool("age <= 12"): 
  print('Je mag naar binnen')

if True: # maak de conditie correct!
  print('welkom')
else:
  print('sorry, niet welkom')
