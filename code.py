import requests
from bs4 import BeautifulSoup
import csv

url_categorie = "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
reponse = requests.get(url_categorie)
page = reponse.text
soup = BeautifulSoup(page, "html.parser")
# obtention du code de la page de la catégorie:

url_livres = soup.find_all("h3")
url_livres_liste = []
for h3 in url_livres:
    a = h3.find("a")
    url_livre = a["href"]
    str(url_livre)
    url_livres_liste.append("https://books.toscrape.com/" + url_livre[9:])
# récupération de l'url des différents livres de la page

for url in url_livres_liste:
    reponse2 = requests.get(url)
    page2 = reponse2.content
    soup2 = BeautifulSoup(page2, "html.parser")

# création d'une boucle pour parcourir les différents livres

    upcs = soup.find_all("td" in "table", class_="table table-striped")[0]
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

    if soup.find("p", class_="star-rating Three"): True
    aviss = "review rating 3/5"
    avis_liste = []
    for avis in aviss:
        avis_liste.append(aviss)
# création d'une boucle qui gère le review rating

    url_img_relatif = soup.img['src']
    url_img_absolu = ("https://books.toscrape.com/" + url_img_relatif[6:])
#recupération de l'url de l'image du livre

en_tete = ["product_page_url", "upc", "title", "price_including_tax", "price_excluding_tax", "number_avaible", "product_description", "category", "review_rating", "image_url"]
# ici upc signifie Universal Product Code

with open("data.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    for upc, titre, prix_ttc, prix_ht, stock, description, categorie, avis, url_img in zip(upcs_liste, titre_textes, prix_ttc_liste, prix_ht_liste, stocks_liste, description_textes, categories_liste, avis_liste, url_img_absolu):
        writer.writerow([url, upc, titre, prix_ttc, prix_ht, stock, description, categorie, avis, url_img_absolu])
# création du fichier csv pour stocker les données
