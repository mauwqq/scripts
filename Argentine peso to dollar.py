import requests
from bs4 import BeautifulSoup
import re 


# Imports html to scrape data
URL = "https://dolarhoy.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Splits dolar value and ask user for correct operation
dolar = soup.find("div", "val").text.split("'")[0]
print("el dolar esta: " + dolar)
print("1-Peso Argentino a Dolar \n2-Dolar a Peso Argentino")
conversor = int(input("Seleccione el tipo de conversion: "))

# Converts string "Dolar" into Integers
dolar_int = int(re.search('[0-9]+',dolar).group(0))

# Quick maths
if conversor >1:
    dolar1 = int(input("Inserte el monto en Dolares: "))
    resultado2 = dolar_int * dolar1
    print(str(dolar1) + " Dolares son: " + str(resultado2) + " Pesos Argentinos")
else:
    peso1 = int(input("Inserte el monto en Pesos Argentinos: "))
    resultado1 = peso1 // dolar_int
    print(str(peso1) + " Pesos Argentinos son: " + str(resultado1) + " Dolares")