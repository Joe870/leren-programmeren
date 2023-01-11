from fruitmand import fruitmand
rond = 0
niet_rond = 0
kleur = ''
while kleur not in fruitmand:
    kleur = input('which color do you choose?')
    for fruit in fruitmand:
        if fruit['color'] == kleur:
            if fruit['round'] == True:
                rond+=1 
            else:
                niet_rond+=1

print(rond)
print(niet_rond)
verschil_rond = abs(rond - niet_rond)
if rond > niet_rond:
    print(f'er zijn {verschil_rond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
elif niet_rond > rond:
    print(f'er zijn {verschil_rond} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
else:
    print(f'er zijn {rond} ronde vruchten en {niet_rond} niet ronde vruchten in de kleur {kleur}')

    
