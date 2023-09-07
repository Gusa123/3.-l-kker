

hus ={"harry": "griffing",
      "hermine": "griffin",
      "ronny": "griffin",
      "draco": "smygard"
}

#eks 1
print(hus["draco"]) #her får vi kun "smygard", ikke draco


#eks 2
for elev in hus:
    print(elev, hus[elev]) #her får vi først elevens navn så huset

#eks 3
for elev in hus:
    print(f"{elev}: {hus[elev]}")