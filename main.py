import datetime

import pytz

#methode 1
heure_actuelle =datetime.datetime.now().strftime(("%H:%M:%S"))
#print("L'heure actuelle est :", heure_actuelle)

#methode2

    # obtention de la date et l'heure actuelle
heure_locale =datetime.datetime.now()
    #definition du fuseau horaire cible
fuseau_cible=pytz.timezone("Europe/Paris")
    #application du zonage sur la date et l'heure
heure_cible=heure_locale.astimezone(fuseau_cible)
    #extraire l'heure dans le fuseau horaire cible
heure= heure_cible.strftime("%H:%M:%S")
print("L'heure actuelle dans le fuseau horaire est :", heure)


    
