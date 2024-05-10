# Gestion des packages Python
import os.path
import requests
from bs4 import BeautifulSoup
import csv

# Création d'un premier objet soup global
url_site = "https://books.toscrape.com/index.html"
response_site = requests.get(url_site)
page_site = response_site.text
soup_site = BeautifulSoup(page_site, "html.parser")

# Création d'une liste de lien par catégories
url_categorie_liste = []
url_categories = soup_site.find_all("a")[3:53]
for url_categorie in url_categories:
    url_categorie = "https://books.toscrape.com/" + url_categorie["href"]
    url_categorie_liste.append(url_categorie)


# Définition d'une fonction recherchant les url des livres
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
    url_livre_liste = []
    search_url(url_categorie)
    print("Fetching " + f"{url_categorie}")

    # Récupération de la catégorie du livre
    categorie = url_categorie.split("/")[6]
    categorie = categorie[:-2]

    # Création, si besoin des dossiers utlisés par notre script pour organiser les données collectées et les images téléchargées

    # Création du dossier principal
    dossier_principal = "Books_to_Scrape_Datas"
    if not os.path.exists(dossier_principal):
        os.makedirs(dossier_principal)

    # Création du dossier de données
    dossier_datas = os.path.join(dossier_principal, "Datas")
    if not os.path.exists(dossier_datas):
        os.makedirs(dossier_datas)

    # Création du dossier pour les images
    dossier_imgs = os.path.join(dossier_principal, "Images")
    if not os.path.exists(dossier_imgs):
        os.makedirs(dossier_imgs)

    # Création des dossiers par catégories, pour et les images
    dossier_img = str(categorie) + "_img"
    dossier_img = os.path.join(dossier_imgs, dossier_img)
    if not os.path.exists(dossier_img):
        os.makedirs(dossier_img)

    # Création des dossiers par catégories, pour et les données
    dossier_data = str(categorie) + "_data"
    dossier_data = os.path.join(dossier_datas, dossier_data)
    if not os.path.exists(dossier_data):
        os.makedirs(dossier_data)

    # Création d'un fichier csv pour stocker les données
    en_tete = ["product_page_url", "upc", "title", "price_including_tax", "price_excluding_tax", "number_avaible",
               "product_description", "category", "review_rating", "image_url"]
    path_data = os.path.join(dossier_data, categorie + ".csv")
    with open(path_data, "w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(en_tete)

        # création d'une boucle pour parcourir les différents livres
        for url_livre in url_livre_liste:
            print("Fetching " + f"{url_livre}")
            # Définition d'un objet soup par livre
            response_2 = requests.get(url_livre)
            page_2 = response_2.content
            soup_2 = BeautifulSoup(page_2, "html.parser")

            # Récupération de l'upc du livre
            upc = soup_2.find_all("td")[0].text

            # Récupération du prix ttc du livre
            prix_ttc = soup_2.find_all("td")[2].text

            # Récupération du prix ht du livre
            prix_ht = soup_2.find_all("td")[3].text

            # Récupération du stock du livre
            stock = soup_2.find_all("td")[5].text

            # Récupération du titre du livre
            titre = soup_2.find("h1").text

            # Récupération de la description du livre
            description = soup_2.find_all("p")[3].text

            # Récupération de l'avis du livre
            avis = soup_2.find("p", class_="star-rating")["class"]
            avis = str(avis)[2:13] + " " + str(avis)[17:-2]

            # Récupération de l'url de l'image du livre
            url_img = soup_2.img['src']
            url_img = str(url_img)
            url_img = "https://books.toscrape.com/" + url_img[6:]


            # Stockage des données dans le fichier csv
            writer.writerow([url_livre, upc, prix_ttc, prix_ht, stock, titre, description, categorie, avis, url_img])

            # Téléchargement de l'image du livre
            response_img = requests.get(url_img)
            if response_img.status_code == 200:
                special_chars = ["?", "/", ":", "*", "\"", "<", ">", "|"]
                for char in special_chars:
                    titre = titre.replace(char, "_")
                titre_split = titre.split(" ")[0:8]
                titre_str = "_".join(titre_split)
                path_img = os.path.join(dossier_img, titre_str + ".jpg")
                with open(path_img, "wb") as fichier_img:
                    fichier_img.write(response_img.content)
            else:
                print("Erreur lors du téléchargement de l'image")
