import requests

url = "https://restcountries.com/v3.1/all?fields=name"
odgovor = requests.get(url)
drzave = odgovor.json()

# 1: Poišči državo z največ sosedi (borders)
# Namig: Nekatere države so otoki in nimajo ključa "borders"!
def one():
    dr = []

    for drzava in drzave:
        dr.append(drzava.get("name").get("official"))

    max_sosedje = 0
    drzava_max_sosedje = ""

    for d in dr:
        c = requests.get(f"https://restcountries.com/v3.1/name/{d}").json()
        borders = c[0].get("borders")
        if borders:
            num_borders = len(borders)
            if num_borders > max_sosedje:
                max_sosedje = num_borders
                drzava_max_sosedje = d

    print(f"Država z največ sosedi je {drzava_max_sosedje} z {max_sosedje} sosedami.")

# 2: Poišči države kjer govorijo največ jezikov (languages)
# Namig: Nekatere države nimajo ključa "languages"
def two():
    dr = []

    for drzava in drzave[:10]:
        dr.append(drzava.get("name").get("official"))
    
    max_lang = 0
    drzava_max_lang = ""

    for d in dr:
        c = requests.get(f"https://restcountries.com/v3.1/name/{d}").json()
        languages = c[0].get("languages")
        if languages:
            num_languages = len(languages)
            if num_languages > max_lang:
                max_lang = num_languages
                drzava_max_lang = d

    print(f"Država z največ jeziki je {drzava_max_lang} z {max_lang} jeziki.")

# 3: Izračunaj povprečno število prebivalcev (population) po celinah (continents)
# Namig: Vedno preveri, če je population večji od 0
def three():
    pass

# 4: Poišči državo z največ časovnimi pasovi (timezones)
# Namig: Vsaka država ima vsaj en timezone
def four():
    pass

# 5: Izpiši vse države, ki imajo v imenu presledek
# Namig: Uporabi ["name"]["common"] za ime države
def five():
    pass

# 6: Izpiši število držav, ki imajo za uradni jezik angleščino
def six():
    pass

# 7: V katerem časovnem pasu (timezone) je največ držav?
# Namig: Ena država ima lahko več timezone-ov
def seven():
    pass

# 8: Katera črka se največkrat pojavi kot prva črka v imenu države?
# Namig: Za ime uporabi ["name"]["common"].lower()
def eight():
    pass

# 9: Katera država ima najdaljše ime?
def nine():
    pass

# 10: Izračunaj še eno statistiko po želji.
def ten():
    pass



two()