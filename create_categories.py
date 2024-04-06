from oscar.apps.catalogue.categories import create_from_breadcrumbs

#define the categories list 

categories = [
    'Téléviseurs > Smart TV',
    'Téléviseurs > Android TV',
    'Téléviseurs > LED TV',

    'Réfrigérqteur > Réfrigérateur Vitrine',
    'Réfrigérqteur > Réfrigérateur Side-by-side ',

    'Congélateur > Congélateur vertical',
    'Congélateur > Congélateur vitrine',

    'Cuisine > Cuisiniére',
    'Cuisine > Four',
    'Cuisine > Micro-ondes',
    'Cuisine > Blenders',
    'Cuisine > Hotte Aspirante',
    'Cuisine > Plaque de cuisson',
    'Cuisine > Lave vaisselle',
    'Cuisine > Fontaine',

    'Climatisation > Air Cooler',
    'Climatisation > Chauffe eau ',

    'Machine à laver > Séche ligne ',
    'Machine à laver > Lavage ',

    
]


for breadcrumbs in categories:
    create_from_breadcrumbs(breadcrumbs)

print ("categories succesfuly  added")