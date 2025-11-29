import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    # Načte obsah stranky
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Stahovani {url} selhalo s kodem {response.status_code}")

    hrefs = []
    html = response.text
    html_lower = html.lower()  # HTML tagy nejsou case-sensitive
    pozice_kurzoru = 0

    # Najde <a ... href="..."> a vytáhne hodnotu href
    while pozice_kurzoru < len(html):

            # Hledáme začátek dalšího tagu <a
        a_pozice = html_lower.find('<a ', pozice_kurzoru)

            # Pokud neni dalsi <a, ukoncime hledani
        if a_pozice == -1: 
            break

            # Najdeme konec tohoto <a ...> tagu
        konec_tagu_pozice = html_lower.find('/a>', a_pozice)
        
            # Pokud neni konec tagu, ukoncime hledani
        if konec_tagu_pozice == -1: 
            break

            # Uvnitř tagu hledáme atribut href
        href_pozice = html_lower.find('href', a_pozice, konec_tagu_pozice)
        if href_pozice == -1:
            pozice_kurzoru = konec_tagu_pozice + 1 # Posuneme kurzor za tento tag
            continue

            # Po href hledáme znak =
        rovnase_pozice = html_lower.find('=', href_pozice, konec_tagu_pozice)
        if rovnase_pozice == -1:
            pozice_kurzoru = konec_tagu_pozice + 1 # Posuneme kurzor za tento tag
            continue

            # Najdeme začátek hodnoty href
        start = rovnase_pozice + 1
        while start < konec_tagu_pozice and html_lower[start].isspace():
            start += 1
        if start >= konec_tagu_pozice:      # Pokud je herf prazdný, pokracujeme dal
            pozice_kurzoru = konec_tagu_pozice + 1
            continue

        quote = html[start]
        if quote in ('"', "'"):
                # Hodnota href je v uvozovkach, vezmeme text mezi nimi
            end = html.find(quote, start + 1, konec_tagu_pozice) # Najdeme konec uvozovek
            if end == -1:
                pozice_kurzoru = konec_tagu_pozice + 1 # Pokud neni konec uvozovek, pokracujeme dal
                continue
            href = html[start + 1:end]
        else:
            # Hodnota href konci prvni mezerou nebo koncem tagu
            end = start
            while end < konec_tagu_pozice and not html[end].isspace():
                end += 1
            href = html[start:end]

        # Přidáme nalezenou hodnotu a posuneme se za aktuální tag
        hrefs.append(href)
        pozice_kurzoru = konec_tagu_pozice + 1

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        print(len(download_url_and_get_all_hrefs(url)))
        print(download_url_and_get_all_hrefs(url))
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
