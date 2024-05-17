Ce fichier README a été généré le [2024-04-19] par [MULLER Jérémy].

Dernière mise-à-jour le : [2024-04-19].

# INFORMATIONS GENERALES

## Titre du jeu de données : Programme d'extraction des prix
 
## Adresse de contact : jeremymuller92@gmail.com
 
# INFORMATIONS METHODOLOGIQUES

## Conditions environnementales / expérimentales : 
Veuillez vous assurer de la qualité de votre connexion internet. Il est recommandé de créer un environnement virtuel et d'y installer les paquets python cités dans le fichier "requirements.txt".

Pour créer un environnement virtuel tapez dans un terminal:

    python -m venv <environment name>

Ensuite, pour activer cet environnement :

    <nom_de_l'environnement>\Scripts\activate (sous Windows)

    source <nom_de_l'environnement>/bin/activate (sous macOS/Linux)

Enfin, installez les dépendances :

    pip install -r requirements.txt

## Description des sources et méthodes utilisées pour collecter et générer les données :

Le script extrait les données des livres listés sur le site "books.toscrape.com". Il parcourt les différentes catégories de livres, récupère les URLs des pages de chaque livre, et collecte des informations telles que le titre, le prix, la disponibilité, la description, la catégorie, l'évaluation et l'image associée.

## Méthodes de traitement des données :

    - Extraction des URls des catégories de livres.

    - Extraction des URLS de chaque livre dans chaque catégorie.

    - Récupération des données souhaitées pour chaque livre: (titre, prix, description, stock, avis, etc.).

    - Sauvegarde des données dans des fichiers csv distincts pour chaque catégorie.

    - Téléchargement des images de chaque livres. 

## Procédures d’assurance qualité appliquées sur les données :

Les URLs collectées sont contrôlées pendant la collecte de données. Les téléchargements, ainsi que les réponses HTTP sont vérifiés, de sorte à assurer la validité des données sauvegardées. Les caractères spéciaux ont été pris en compte et modifiés, pour éviter qu'ils ne générent des conflits dans la nomination des fichiers images notamment. Tout problème est signalé dans la console lors de l'exécution.


# APERCU DES DONNEES ET FICHIERS


## Convention de nommage des fichiers :

Les fichiers de données sont nommés selon le schéma suivant : <categorie>_data.csv pour les données et <categorie>_img/ pour les images.

## Arborescence/plan de classement des fichiers :

Books_to_Scrape_Datas/
    Data/
        <catégorie>_data/
            <catégorie>.csv

    Images/
        <catégorie>_img/
            <titre_du_livre>.jpg

# INFORMATIONS SPECIFIQUES AUX DONNEES POUR : [NOM DU FICHIER]


## Liste des variables/en-têtes de colonne :

- "product_page_url" : URL de la page du produit

- "upc" : Universal Product Code (code produit unique en français)

- "title" : Titre du livre

- "price_including_tax" : Prix TTC

- "price_excluding_tax" : Prix HT

- "number_avaible" : Quantité disponible

- "product_description" : Description du livre

- "category" : Catégorie du livre

- "review_rating" : Note du livre sur 5

- "image_url" : URL de l'image de couverture du livre



## Informations additionnelles : 

Il s'agit d'un script conçu et adapté à l'architecture du site "books.toscrape.com". Si celle-ci venait à changer, le script pourrait rencontrer des dysfonctionnements. 

Il est important de noter que les paquets suivants sont nécessaires pour le bon fonctionnement de ce script : 
    - Python 3.x
    - BeautifulSoup4
    - requests
    - csv

