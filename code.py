import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/catalogue/unicorn-tracks_951/index.html"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, "html.parser")

upcs = soup.find_all("td", {"data-title": "UPC"})
print(upcs)

titres = soup.find_all("li", class_="active")
titre_textes = []
for titre in titres:
    titre_textes.append(titre.string)
# recupération du titre du livre

descriptions = soup.find_all("p")[3]
description_textes = []
for description in descriptions:
    description_textes.append(description.string)
# récupération de la description du livre
prix_ht = soup.find()

# récupération du prix hors-taxe du livre
en_tete = ["product_page_url", "upc", "title", "price_including_tax", "price_excluding_tax", "number_avaible", "product_description", "category", "review_rating", "image_url"]
# ici upc signifie Universal Product Code

with open("data.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    for titre, description in zip(titre_textes, description_textes):
        writer.writerow([url, upcs, titre, description])
