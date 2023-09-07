elever= [
    {"navn": "harry",
    "hus": "griffidor",
    "petronus": "hjort"},

    {"navn": "hermine", 
    "hus": "griffindor", 
    "petronus": "jack" },

    {"navn": "ronny",
    "hus": "griffindor",
    "petronus": "katt"},

    {"navn": "draco",
    "hus": "smygard",
    "petronus": None}
]

#eks 1
print(elever[2]["hus"])

#eks 2
for elev in elever:
    print (elev["navn"], elev["hus"], elev["petronus"], sep=",")
