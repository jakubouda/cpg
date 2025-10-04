#
# První úloha podle e-learningu
#

###
# Funkce sudy_nebo_lichy vrací True, pokud je parametr sudý, False, pokud je parametr lichý
###
def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    cislo = input("Zadejte cislo:" )
    cislo = int(cislo)
    if sudy_nebo_lichy(cislo):
        print(f"Cislo {cislo} je sude.")
    else:
        print(f"Cislo {cislo} je liche.")