import httpx

print("Obchodni prevodnik")

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=13.02.2025"

r = httpx.get(url)
#print(r.text)

in_array = r.text.split("\n")

#print(in_array)

for line in in_array:
    if "|EUR|" in line:
        print(line)
        
castka = input("Zadej castku v CZK: ")
result = int(castka) / 25
print(f"To je v EUR:  {result}")
castaka2 = input("Zadejte castku v CZK: ")
result2 = int(castaka2) * 25
print(f"To je v CYK:  {result2}")