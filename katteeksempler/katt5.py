def  main():
    n = hent_antall_katter()
    print_mjau(n)

def hent_antall_katter():
    while True:
        antall= int(input("hvor mange katter ar du?"))
        if antall> 0:
            return antall

def print_mjau(antall):
    print("mjau\n" * antall, end="")  

main()