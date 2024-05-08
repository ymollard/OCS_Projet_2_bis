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
url_categories = soup_site.find_all("a")[3:6]
for url_categorie in url_categories:
    url_categorie = "https://books.toscrape.com/" + url_categorie["href"]
    url_categorie_liste.append(url_categorie)

    # Création d'une liste de pages par catégories à régler!
    if soup_site.find("ul", class_="pager"):
        lien_next = soup.find("li", class_="next")
        if lien_next:
            lien_next = lien_next.find("a")["href"]
            path = "/".join(url_categorie.split("/")[:-1]) + "/"
            lien_next = path + lien_next
            url_categorie_liste.append(lien_next)

# Définition d'une fonction recherchant les URL de livres
url_livre_liste = []
def search_url(url_page):
    response_page = requests.get(url_page)
    page = response_page.text
    soup_page = BeautifulSoup(page, "html.parser")
    url_livres = soup_page.find_all("h3")
    for h3 in url_livres:
        url_livre = h3.find("a")
        url_livre = url_livre["href"]
        url_livre = str(url_livre)
        url_livre = "https://books.toscrape.com/catalogue/" + url_livre[9:]
        url_livre_liste.append(url_livre)



