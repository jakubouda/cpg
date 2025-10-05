#
# Druhá úloha podle e-learningu
#


###
# Funkce vrací string, převádí číselný parametr na slovní vyjádření hodnoty
###
def cislo_text(cislo):
    if cislo == 0:
        return "nula"
    else:

        desitky = int(cislo/10)                     
        jednotky = cislo % 10
        vysledek = ""

        if 10 >= cislo or cislo >= 20:
            match desitky:
                case 1:
                    vysledek += "deset"
                case 2:
                    vysledek += "dvacet"
                case 3:
                    vysledek += "třicet"
                case 4:
                    vysledek += "čtyřicet"
                case 5:
                    vysledek += "padesát"
                case 6:
                    vysledek += "šedesát"
                case 7:
                    vysledek += "sedmdesát"
                case 8:
                    vysledek += "osmdesát"
                case 9:
                    vysledek += "devadesát"
                case 10:
                    vysledek += "sto"
            
            #připojení mezery mezi slovy, pokud je potřeba
            if not jednotky == 0 and not desitky == 0:
                vysledek += " "

            match jednotky:
                case 1:
                    vysledek += "jedna"
                case 2:
                    vysledek += "dva"
                case 3:
                    vysledek += "tři"
                case 4:
                    vysledek += "čtyři"
                case 5:
                    vysledek += "pět"
                case 6:
                    vysledek += "šest"
                case 7:
                    vysledek += "sedm"
                case 8:
                    vysledek += "osm"
                case 9:
                    vysledek += "devět"
            return vysledek
        else:
            match cislo:
                case 11:
                    return "jedenáct"
                case 12:
                    return "dvanáct"
                case 13:
                    return "třináct"
                case 14:
                    return "čtrnáct"
                case 15:
                    return "patnáct"
                case 16:
                    return "šestnáct"
                case 17:
                    return "sedmnáct"
                case 18:
                    return "osmnáct"
                case 19:
                    return "devatenáct"




if __name__ == "__main__":
    cislo = input("Zadejte cislo: ")
    cislo = int(cislo)
    if 0 <= cislo <= 100:
        print(cislo_text(cislo))

    else:
        print("Číslo musí být v rozmezí 0 až 100.")
