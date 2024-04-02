from oscar.apps.catalogue.categories import create_from_breadcrumbs

#define the categories list 

categories = [
    'Gros Electromenagers > Appareils de cuisson',
    'Gros Electromenagers > Gaziniére',
    'Gros Electromenagers > Congélateurs',
    'Gros Electromenagers > Réfrigérateurs',
    'Gros Electromenagers > Laveuses et sécheuses',

    'Appareils Menagers > Appareils de cuisine',
    'Appareils Menagers > Appareils de santé et de beauté',
    'Appareils Menagers > Luminaires & éclairage',
    'Appareils Menagers > Nettoyeurs & Aspirateurs ',
    "Appareils Menagers > Qualité de l\'air et appareils saisonniers",

    'Petits Electromenagers > Préparation des boissons',
    'Petits Electromenagers > Bouilloires',
    'Petits Electromenagers > Mélangeurs et mixeurs',
    'Petits Electromenagers > Repassage et blanchisserie',
    'Petits Electromenagers > Aspirateurs',
    'Petits Electromenagers > Autres petits appareils',
    
]


for breadcrumbs in categories:
    create_from_breadcrumbs(breadcrumbs)

print ("categories succesfuly  added")