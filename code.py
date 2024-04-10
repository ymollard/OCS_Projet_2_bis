import requests
from bs4 import BeautifulSoup
import csv

# obtention du code de la page de la catégorie:
url_categorie = "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
reponse = requests.get(url_categorie)
page = reponse.text
soup = BeautifulSoup(page, "html.parser")

# récupération de l'url des différents livres de la page
url_livres = soup.find_all("h3")
url_livres_liste = []
for h3 in url_livres:
    a = h3.find("a")
    url_livre = a["href"]
    url_livre = str(url_livre)
    url_livres_absolue = "https://books.toscrape.com/catalogue/" + url_livre[9:]
    url_livres_liste.append(url_livres_absolue)

# création d'une boucle pour parcourir les différents livres
for url_livres_absolue in url_livres_liste:
    reponse2 = requests.get(url_livres_absolue)
    page2 = reponse2.content
    soup2 = BeautifulSoup(page2, "html.parser")

# recupération de l'upc du livre
    upcs = soup2.find_all("td")[0]
    upcs_liste = []
    for upc in upcs:
        upcs_liste.append(upc.text)

# recupération du prix ttc du livre
    prix_s_ttc = soup2.find_all("td")[2]
    prix_ttc_liste = []
    for prix_ttc in prix_s_ttc:
        prix_ttc_liste.append(prix_ttc)

# recupération du prix ht du livre
    prix_s_ht = soup2.find_all("td")[3]
    prix_ht_liste = []
    for prix_ht in prix_s_ht:
        prix_ht_liste.append(prix_ht)

# recupération du stock du livre
    stocks = soup2.find_all("td")[5]
    stocks_liste = []
    for stock in stocks:
        stocks_liste.append(stock)

# recupération du titre du livre
    titres = soup2.find_all("h1")
    titre_textes = []
    for titre in titres:
        titre_textes.append(titre.string)

# récupération de la description du livre
    descriptions = soup2.find_all("p")[3]
    description_textes = []
    for description in descriptions:
        description_textes.append(description.string)


# recupération de la catégorie du livre
    categories = soup2.find_all("a")[3]
    categories_liste = []
    for categorie in categories:
        categories_liste.append(categorie)

# récupération du "review rating" du livre
    aviss = soup2.find_all("p", class_="star-rating")
    if aviss:
        premieravis = aviss[0]
        if "Three" in premieravis["class"]:
            avis = "Ce livre est noté 3/5"
        elif "One" in premieravis["class"]:
            avis = "Ce livre est noté 1/5"
        elif "Two" in premieravis["class"]:
            avis = "Ce livre est noté 2/5"
        elif "Four" in premieravis["class"]:
            avis = "Ce livre est noté 4/5"
        elif "Five" in premieravis["class"]:
            avis = "Ce livre est noté 5/5"
    else:
        avis = "Ce livre n'est pas noté"
    avis_liste = []
    for i in (len(url_livres_liste)):
        avis_liste.append(aviss)
    print(avis_liste)


# recupération de l'url de l'image du livre
    url_img_relatif = soup2.img['src']
    url_img_relatif = str(url_img_relatif)
    url_img_absolues = "https://books.toscrape.com/" + url_img_relatif[6:]
    url_img_liste = []
    for i in range(len(url_livres_liste)):
        url_img_liste.append(url_img_absolues)

en_tete = ["product_page_url", "upc", "title", "price_including_tax", "price_excluding_tax", "number_avaible", "product_description", "category", "review_rating", "image_url"]
# ici upc signifie Universal Product Code

# création du fichier csv pour stocker les données
with open("data.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    for url_livre, upc, titre, prix_ttc, prix_ht, stock, description, categorie, url_img in zip(url_livres_liste, upcs_liste, titre_textes, prix_ttc_liste, prix_ht_liste, stocks_liste, description_textes, categories_liste, url_img_absolu):
        writer.writerow([url_livre, upc, titre, prix_ttc, prix_ht, stock, description, categorie, url_img_absolu])

