import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/catalogue/unicorn-tracks_951/index.html"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, "html.parser")

upcs = soup.find_all("td")[0]
upcs_liste = []
for upc in upcs:
    upcs_liste.append(upc)
# recupération de l'upc du livre

prix_s_ttc = soup.find_all("td")[2]
prix_ttc_liste = []
for prix_ttc in prix_s_ttc:
    prix_ttc_liste.append(prix_ttc)
# recupération du prix ttc du livre

prix_s_ht = soup.find_all("td")[3]
prix_ht_liste = []
for prix_ht in prix_s_ht:
    prix_ht_liste.append(prix_ht)
# recupération du prix ht du livre

stocks = soup.find_all("td")[5]
stocks_liste = []
for stock in stocks:
    stocks_liste.append(stock)
# recupération du stock du livre

titres = soup.find_all("h1")
titre_textes = []
for titre in titres:
    titre_textes.append(titre.string)
# recupération du titre du livre

descriptions = soup.find_all("p")[3]
description_textes = []
for description in descriptions:
    description_textes.append(description.string)
# récupération de la description du livre

categories = soup.find_all("a")[3]
categories_liste = []
for categorie in categories:
    categories_liste.append(categorie.string)
# recupération de la catégorie du livre

avis = soup.p['class']
print(avis)

# recupération des avis du livre

# recupération de l'url de l'image du livre


en_tete = ["product_page_url", "upc", "title", "price_including_tax", "price_excluding_tax", "number_avaible", "product_description", "category", "review_rating", "image_url"]
# ici upc signifie Universal Product Code

with open("../data.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    for upc, titre, prix_ttc, prix_ht, stock, description, categorie in zip(upcs_liste, titre_textes, prix_ttc_liste, prix_ht_liste, stocks_liste, description_textes, categories_liste):
        writer.writerow([url, upc, titre, prix_ttc, prix_ht, stock, description, categorie])
# création du fichier csv pour stocker les données
