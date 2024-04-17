import requests
from bs4 import BeautifulSoup
import csv

# création d'un premier objet soup
url_site = "https://books.toscrape.com/index.html"
reponse_site = requests.get(url_site)
page_site = reponse_site.text
soup_site = BeautifulSoup(page_site, "html.parser")
# création d'une liste de lien par catégories
url_categorie_liste = []
url_categories = soup_site.find_all("a")[3:10]
for url_categorie in url_categories:
    url_categorie = "https://books.toscrape.com/" + url_categorie["href"]
    url_categorie_liste.append(url_categorie)

# récupération de tous les liens des livres d'une catégorie
for url_categorie in url_categorie_liste:
    reponse = requests.get(url_categorie)
    page = reponse.text
    soup = BeautifulSoup(page, "html.parser")

    # récupération de l'url des différents livres de la page
    url_livres_liste = []
    url_livres = soup.find_all("h3")
    for h3 in url_livres:
        a = h3.find("a")
        url_livre = a["href"]
        url_livre = str(url_livre)
        url_livres_absolue = "https://books.toscrape.com/catalogue/" + url_livre[9:]
        url_livres_liste.append(url_livres_absolue)
    # prise en compte de la pagination:
    if soup.find("ul", class_="pager"):
        lien_next = soup.find("li", class_="next")
        if lien_next:
            lien_next = lien_next.find("a")["href"]
            path = '/'.join(url_categorie.split('/')[:-1]) + '/'
            lien_next = path + lien_next
            url_categorie_liste.append(lien_next)

    upcs_liste = []
    prix_ttc_liste = []
    prix_ht_liste = []
    stocks_liste = []
    titre_textes = []
    description_textes = []
    categories_liste = []
    avis_liste = []
    url_img_liste = []
    # création d'une boucle pour parcourir les différents livres
    for url_livres_absolue in url_livres_liste:
        reponse2 = requests.get(url_livres_absolue)
        page2 = reponse2.content
        soup2 = BeautifulSoup(page2, "html.parser")

    # recupération de l'upc du livre
        upc = soup2.find_all("td")[0].text
        upcs_liste.append(upc)
    # recupération du prix ttc du livre
        prix_ttc = soup2.find_all("td")[2].text
        prix_ttc_liste.append(prix_ttc)
    # recupération du prix ht du livre
        prix_ht = soup2.find_all("td")[3].text
        prix_ht_liste.append(prix_ht)
    # recupération du stock du livre
        stock = soup2.find_all("td")[5].text
        stocks_liste.append(stock)
    # recupération du titre du livre
        titre = soup2.find("h1").text
        titre_textes.append(titre)
    # récupération de la description du livre
        description = soup2.find_all("p")[3].text
        description_textes.append(description)
    # recupération de la catégorie du livre
        categorie = soup2.find_all("a")[3].text
        categories_liste.append(categorie)
    # récupération du "review rating" du livre
        avis = soup2.find("p", class_="star-rating")["class"]
        avis = str(avis)[2:13] + " " + str(avis)[17:-2]
        avis_liste.append(avis)
    # recupération de l'url de l'image du livre
        url_img = soup2.img['src']
        url_img = str(url_img)
        url_img = "https://books.toscrape.com/" + url_img[6:]
        url_img_liste.append(url_img)
    print(avis_liste)

    # création du fichier csv pour stocker les données
    en_tete = ["product_page_url", "upc", "title", "price_including_tax", "price_excluding_tax", "number_avaible", "product_description", "category", "review_rating", "image_url"]
    with open("data.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(en_tete)
        for i in range(len(url_livres_liste)):
            url_livre = url_livres_liste[i]
            upc = upcs_liste[i]
            titre = titre_textes[i]
            prix_ttc = prix_ttc_liste[i]
            prix_ht = prix_ht_liste[i]
            stock = stocks_liste[i]
            description = description_textes[i]
            categorie = categories_liste[i]
            avis = avis_liste[i]
            url_img = url_img_liste[i]
            writer.writerow([url_livre, upc, titre, prix_ttc, prix_ht, stock, description, categorie, avis, url_img])

