import httpx

def ziskat_kurz():
    url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
    try:
        r = httpx.get(url)
        r.raise_for_status()
        lines = r.text.split("\n")
        for line in lines:
            if "|EUR|" in line:
                row_arr = line.split("|")
                kurz_str = row_arr[-1].replace(",", ".")
                return float(kurz_str)
    except Exception as e:
        print(f"Chyba při načítání kurzu: {e}")
        return None

def prevod_meny():
    kurz = ziskat_kurz()
    if kurz is None:
        print("Nepodařilo se získat aktuální kurz.")
        return
    
    while True:
        volba = input("Vyber směr převodu (1: EUR -> CZK, 2: CZK -> EUR): ")
        if volba not in ["1", "2"]:
            print("Neplatná volba, zkuste to znovu.")
            continue
        
        try:
            castka = float(input("Zadej částku: "))
            if castka < 0:
                print("Částka musí být kladné číslo.")
                continue
        except ValueError:
            print("Neplatný vstup, zadejte číslo.")
            continue
        
        if volba == "1":
            vysledek = castka * kurz
            print(f"{castka} EUR odpovídá {vysledek:.2f} CZK.")
        else:
            vysledek = castka / kurz
            print(f"{castka} CZK odpovídá {vysledek:.2f} EUR.")
        
        break

if __name__ == "__main__":
    prevod_meny()
