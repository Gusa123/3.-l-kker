# # 3.1 --------

# temp= float(input("hva er din kropstempratur?"))

# if temp > 36.5:
#     print("du har en høyere kropstempratur en normal, du er syk")
# elif temp < 37.5:
#     print("du har en mindre kropstempratur en normal, du er syk")
# else:
#     print("du har normal kropstempratur")



# #3.2-------
# 1.
# tall= input("skriv en fargekode")
# r, g, b= tall.split(" ")

# if r.isnumeric() and g.isnumeric() and b.isnumeric():
#     r= int(r)
#     g= int(g)
#     b= int(b)

#     if 0 <= r >= 255 and 0<= g >= 255 and 0<= b >= 255:
#         print("gyldig fargekode")
#     else:
#         print("ugyldnig fargekode")

# # else:
#     print("fargen må være et tall")


# #3.4--------

# #1.
# for i in range(11):
#     print(i)

# #2.
# tall= -1
# while True:
#     if tall <10:
#         tall=tall+1
#         print(tall)
#     else:
#         break

# # #3
# liste = ["Sauer", "er", "myke", "dyr."]
# for i in liste:
#     print(i)

# # 4.
# i = 0
# while i < len(liste):
#     print(liste[i])
#     i=i+1



# #3.5--------
# #1.
# #førsye eks på svar
liste= [6, -4, 7, -2, 8, -3, 9, -11]
# minst= liste[0]


# for tall in liste:
#     if tall < minst:
#         minst= tall
# print(minst)
# #andre eksempel på svar
# liste.sort()
# print(liste.sort[0])


# #2.
# størst= liste[0]
# for stor in liste:
#     if stor < størst:
#         størst=stor
# print(stor)


#3.6---------
telefonbok= [
    {"Navn": "Arne",      
     "Tlf": 22334455 },
    {"Navn": "Lisa",        
     "Tlf": 95959595 },
    {"Navn": "Jonas"     
     "Tlf": 97959795 }
]

hvem= input("skriv navnet ditt")
if hvem in telefonbok:
    