# On décompose le programme en repartant de 0

# Gestion des packages Python
import os.path
import requests
from bs4 import BeautifulSoup
import csv

# Création d'un premier objet soup global
url_site = "https://books.toscrape.com/index.html"
reponse_site = requests.get(url_site)
page_site = reponse_site.text
soup_site = BeautifulSoup(page_site, "html.parser")

# Création d'une liste de lien par catégories
url_categorie_liste = []
url_categories = soup_site.find_all("a")[3:7]
for url_categorie in url_categories:
    url_categorie = "https://books.toscrape.com/" + url_categorie["href"]
    url_categorie_liste.append(url_categorie)


# Définition d'une fonction recherchant les URL de livres
url_livre_liste = []
def search_url(link):
    response_link = requests.get(link)
    page = response_link.text
    soup_link = BeautifulSoup(page, "html.parser")
    url_livres = soup_link.find_all("h3")
    for h3 in url_livres:
        url_livre = h3.find("a")
        url_livre = url_livre["href"]
        url_livre = str(url_livre)
        url_livre = "https://books.toscrape.com/catalogue/" + url_livre[9:]
        url_livre_liste.append(url_livre)
    # Prise en compte de la pagination
    if soup_link.find("ul", class_="pager"):
        lien_next = soup_link.find("li", class_="next")
        if lien_next:
            lien_next = lien_next.find("a")["href"]
            path = "/".join(url_categorie.split("/")[:-1]) + "/"
            lien_next = path + lien_next
            search_url(lien_next)

# Création d'une première boucle parcourant les catégories
for url_categorie in url_categorie_liste:
    search_url(url_categorie)


    # Création des dossiers utlisés par notre script
    dossier_img = str(categorie) + "_img"
    if not os.path.exists(dossier_img):
        os.makedirs(dossier_img)
    dossier_data = str(categorie) + "_data"
    if not os.path.exists(dossier_data):
        os.makedirs(dossier_data)
    # Création d'un fichier csv pour sotcker les données
    en_tete = ["product_page_url", "upc", "title", "price_including_tax", "price_excluding_tax", "number_avaible",
               "product_description", "category", "review_rating", "image_url"]
    path_data = os.path.join(dossier_data, categorie + ".csv")
    with open(path_data, "w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(en_tete)
        for i in range(len(url_livres_liste)):
            writer.writerow([url_livres_liste[i], upcs_liste[i], titre_textes[i], prix_ttc_liste[i], prix_ht_liste[i],
                             stocks_liste[i], description_textes[i], categories_liste[i], avis_liste[i],
                             url_img_liste[i]])