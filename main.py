import requests

url = "https://restcountries.com/v3.1/all?fields=name"
odgovor = requests.get(url)
drzave = odgovor.json()

# 1: Poišči državo z največ sosedi (borders)
# Namig: Nekatere države so otoki in nimajo ključa "borders"!
dr = []

for drzava in drzave[:10]:
    dr.append(drzava.get("name").get("official"))
print(dr)

for d in dr:
    c = requests.get(f"https://restcountries.com/v3.1/name/{d}").json()
    print(c[0].get("borders"))

# 2: Poišči države kjer govorijo največ jezikov (languages)
# Namig: Nekatere države nimajo ključa "languages"

# 3: Izračunaj povprečno število prebivalcev (population) po celinah (continents)
# Namig: Vedno preveri, če je population večji od 0

# 4: Poišči državo z največ časovnimi pasovi (timezones)
# Namig: Vsaka država ima vsaj en timezone

# 5: Izpiši vse države, ki imajo v imenu presledek
# Namig: Uporabi ["name"]["common"] za ime države

# 6: Izpiši število držav, ki imajo za uradni jezik angleščino

# 7: V katerem časovnem pasu (timezone) je največ držav?
# Namig: Ena država ima lahko več timezone-ov

# 8: Katera črka se največkrat pojavi kot prva črka v imenu države?
# Namig: Za ime uporabi ["name"]["common"].lower()

# 9: Katera država ima najdaljše ime?

# 10: Izračunaj še eno statistiko po želji.