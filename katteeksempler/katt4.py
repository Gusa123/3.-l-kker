
#eks 1
while True:
    antall= int(input("hvor mange katter har du?")) #blir en evig løkke fordi true alltid er sannt, med mindre du skriver noe som ikke er et tall



#eks 2
while True:
    antall= int(input("hvor mange katter har du?"))
    if antall >0:
        break

for i in range(antall):
    print("mjau")


#eks 3, usikker på om den funker helt
while True:
    antall= input("hvor mange katter har du?")
    er_Tall= antall.isnumeric() #skjekker om det er et tall
    antall= int(antall)
    if er_Tall or antall >0:
        break
    
for i in range(antall):
    print("mjau")