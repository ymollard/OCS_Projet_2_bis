import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/catalogue/unicorn-tracks_951/index.html"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, "html.parser")

titres = soup.find_all("li", class_="active")
titre_textes = []
for titre in titres:
    titre_textes.append(titre.string)

descriptions = soup.find_all("p")
description_textes = []

for description in descriptions:
    description_textes.append(description.string)
"#partons du principe que ça a fonctionné, et que j'ai bien collecté ma description, répétons l'opération pour une autre donnée"

en_tete = ["titre", "description"]
with open("data.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    for titre, description in zip(titre_textes, description_textes):
        writer.writerow([titre, description])
