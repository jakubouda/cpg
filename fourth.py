def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Implementace pravidel pohybu pro různé figury zde.

    typ = figurka.get("typ")
    pozice = figurka.get("pozice")
    for x in obsazene_pozice:   #Vyloučení tahu na obsazenou pozici
        if x == cilova_pozice:
            return False
    if (cilova_pozice[0] > 8 or cilova_pozice[1] > 8) or (cilova_pozice[0] < 1 or cilova_pozice[1] < 1): 
        #Vyloučení tahu mimo šachovnici
        return False
    match typ:
        case "pěšec":
            if (pozice[1] != cilova_pozice[1] or cilova_pozice[0] <= pozice[0]): #Vyloučení tahu mimo pravidla
                return False
            elif (pozice[0] == 2):                                      #tah z výchozí pozice
                for y in obsazene_pozice:
                    if y[0] == pozice[0] + 1 and y[1] == pozice[1]: #žádná obsazená pozice v cestě
                        return False
                return(cilova_pozice[0] <= pozice[0] + 2)
            else:                                                       #tah mimo výchozí pozici
                return(cilova_pozice[0] <= pozice[0] + 1)
            
        case "jezdec":
            if abs(cilova_pozice[0] - pozice[0]) == 2:
                return(abs(cilova_pozice[1] - pozice[1]) == 1)
            if abs(cilova_pozice[0] - pozice[0]) == 1:
                return(abs(cilova_pozice[1] - pozice[1]) == 2)
        case "věž":
            if pozice[0] == cilova_pozice[0]:
                for y in obsazene_pozice:
                    if (y[0] == pozice[0] and y != pozice):
                        if(pozice[1] - y[1] < pozice[1] - cilova_pozice[1]):
                            return False
                return True
            elif pozice[1] == cilova_pozice[1]:
                for y in obsazene_pozice:
                    if (y[1] == pozice[1] and y != pozice):
                        if(pozice[0] - y[0] < pozice[0] - cilova_pozice[0]):
                            return False
                return True
        case "střelec":
            if(abs(cilova_pozice[0] - pozice[0]) == abs(cilova_pozice[1] - pozice[1])):
                for y in obsazene_pozice:
                    if(pozice[0] < y[0] < cilova_pozice[0]) and pozice[0] - y[0] == pozice[1] - y[1]:
                        return False
                    elif(pozice[0] > y[0] > cilova_pozice[0]) and pozice[0] - y[0] == pozice[1] - y[1]:
                        return False
                return True
        case "dáma":
            print("ověřování dáma")

        case "král":
            print("ověřování král")



    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2),(3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}
    """
    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat
    
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici
    """
    print(je_tah_mozny(strelec,(4, 1), obsazene_pozice)) #True
    print(je_tah_mozny(strelec,(8, 5), obsazene_pozice)) #True
    print(je_tah_mozny(strelec,(8, 1), obsazene_pozice)) #True
    print(je_tah_mozny(strelec,(4, 2), obsazene_pozice)) #False
    print(je_tah_mozny(strelec,(1, 8), obsazene_pozice)) #False
    print(je_tah_mozny(strelec,(5, 4), obsazene_pozice)) #False
    """
    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
    
    """
    #print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))
    #je_tah_mozny(jezdec, (4, 4), obsazene_pozice)
    #je_tah_mozny(vez, (8, 1), obsazene_pozice)
    #je_tah_mozny(strelec, (4, 4), obsazene_pozice)
    #je_tah_mozny(dama, (8, 1), obsazene_pozice)
    #je_tah_mozny(kral, (4, 4), obsazene_pozice)