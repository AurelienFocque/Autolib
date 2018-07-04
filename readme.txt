Ces outils permettent de s'interfacer avec le site web d'autolib :

getbills.py [username] [password] permet de récupérer toutes les factures pdf du compte.

getxlsxfile.py [username] [password] permet de récupérer le fichier XL récapitulatif des locations du compte.

parsexlsx.py parse le fichier issu de getxlsxfile.py pour calculer le temps total de location, le prix total des locations et si vous fournissez au code une clé pour l'API google map la distance totale parcourue.
