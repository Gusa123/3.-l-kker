
#eks 1
for elev in ["harry", "hermine", "ronny"]:
    print(elev) #printer en og en elev om gangen

print("ferdig") #når alle elevene i listen er printet går vi ut av for løkken


#eks 2

elever= ["harry", "hermine", "ronny"]
for elev in elever:
    print(elev)


#eks 3 - naiv måte
print(elever[0])
print(elever[1])
print(elever[2])

#eks 4
for i in range(len(elever)): #lengden på listen elever, som er det samme som 3
    print(i+1, elever[i], sep=": ") #om man skriver kun elever får du hele lista. menn ved å putte på [i] får vi navn etter navn

#eks 5
for i in range(len(elever)):
    print(f"{i+1}: {elever[i]}")
     