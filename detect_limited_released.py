# -*- coding: utf-8 -*-
import requests

# URL de l'API - KO err 403
url = "https://realt.co/wp-json/realt/v1/products/for_sale"
# OK 
#url = "https://api.realtoken.community/v1/token/lastUpdate"


try:
    # Effectuer la requête GET avec les paramètres
    response = requests.get(url)
    
    # Vérifier si la requête a été un succès
    response.raise_for_status()

    
    # Afficher le contenu JSON de la réponse
    data = response.json()
    print(data)
    
except requests.exceptions.RequestException as e:
    # Affiche une erreur en cas de problème avec la requête
    print(f"Erreur lors de l'appel à l'API : {e}")
