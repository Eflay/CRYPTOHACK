def fermat():
    base = int(input("Donnez le nombre servant de base : "))
    exp = int(input("Donnez le nombre servant d'exposant : "))
    prime = int(input("Donnez le nombre servant de modulo : "))

    if exp == prime:
        print(base)
    elif exp + 1 == prime and base % prime != 0:
        print(1)


if __name__ == '__main__':
    fermat()