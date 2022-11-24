totaal=0 
cijferlijst = [5,12,19,27,3] 
cijferlijst.append(25)
print(cijferlijst)
print(len(cijferlijst))
cijferlijst.remove(12) 
print(cijferlijst) 
cijferlijst.pop(0)
print(cijferlijst)
cijferlijst.insert(0,36)
print(cijferlijst) 
for som in range(len(cijferlijst)):
    totaal += cijferlijst[som]
print(totaal)
cijferlijst.clear()
print(cijferlijst)
