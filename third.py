import time


def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False
    """
    cislo = int(cislo)
    if cislo <= 1:
        return False
    
    for delitel in range(2, cislo):
        time.sleep(0.001)
        if cislo % delitel == 0:
            return False
    
    return True


def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    maximum = int(maximum)
    results = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            results.append(i)
    return results

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    # 999983
    print(je_prvocislo(cislo))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)