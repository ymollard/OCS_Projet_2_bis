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

Indique comment lancer ton projet. Bien sûr, ce projet est très simple donc n'importe quel pythoniste saura le lancer sans aide mais c'est une bonne idée de donner un exemple explicite. Je pense qu'actuellement tu le lances en cliquant sur le bouton vert de Pycharm, mais la commande générale est python script.py à faire après l'installation du `requirements.txt`

Au lieu de nommer ton script `script.py`, choisis un nom plus précis : Par exemple `drop-bomb-on-pentagon.py` si tu veux attirer l'attention de la NSA, ou bien `scrap-online-books.py` si à tout hasard le rôle de ton script était de scraper des données de livres en ligne. Cela sera particulierement utile si ton projet est amené à grossir et qu'il y a donc plusieurs scripts, il faut les différencier.

## Description des sources et méthodes utilisées pour collecter et générer les données :

Le script extrait les données des livres listés sur le site "books.toscrape.com". Il parcourt les différentes catégories de livres, récupère les URLs des pages de chaque livre, et collecte des informations telles que le titre, le prix, la disponibilité, la description, la catégorie, l'évaluation et l'image associée.

## Méthodes de traitement des données :

    - Extraction des URls des catégories de livres.

    - Extraction des URLS de chaque livre dans chaque catégorie.

    - Récupération des données souhaitées pour chaque livre: (titre, prix, description, stock, avis, etc.).

    - Sauvegarde des données dans des fichiers csv distincts pour chaque catégorie.

    - Téléchargement des images de chaque livres. 

## Procédures d’assurance qualité appliquées sur les données :

 Les téléchargements, ainsi que les réponses HTTP sont vérifiés, de sorte à assurer la validité des données sauvegardées. Les caractères spéciaux ont été pris en compte et modifiés, pour éviter qu'ils ne générent des conflits dans la nomination des fichiers images notamment. Tout problème est signalé dans la console lors de l'exécution.
Que veut dire "Les URLs collectées sont contrôlées pendant la collecte de données." ? Si tu parles de la vérification des codes de statut des réponses HTTP, ce ne sont pas vraiment "les URL" qui sont contrôlées, mais le code de réponse. Et c'est déjà écrit dans la phrase qui suit, il manque juste le terme "code" qui désigne véritablement le numéro (par exemple le code 404 = non trouvé).

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

# INFORMATIONS SPECIFIQUES AUX DONNEES POUR : Mais de quel fichier s'agit-il ?


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

Cette partie sur les dépendances doit être regroupées avec la partie sur requirements.txt car c'est justement le rôle de requirements.txt de lister les dépendances. Toutefois ça ne t'empêche pas de les lsiter dans le README, mais autant le faire au même endroit (et pas à la fin du README car c'est plutôt un prérequis ... donc vers le début).

