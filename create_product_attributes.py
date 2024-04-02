from oscar.apps.catalogue.models import *

# create the nmaterial attributes


material = AttributeOptionGroup.objects.create(name='material')
color = AttributeOptionGroup.objects.create(name='color')


# Assign options to material option group

AttributeOption.objects.create(
    group= material,
    option= 'Steel'
)
AttributeOption.objects.create(
    group= material,
    option= 'Aluminium'
)
AttributeOption.objects.create(
    group= material,
    option= 'Thorium'
)

# Assign option to color option group

AttributeOption.objects.create(
    group= color,
    option= 'Rouge'
)
AttributeOption.objects.create(
    group= color,
    option= 'Bleu'
)
AttributeOption.objects.create(
    group= color,
    option= 'Vert'
)
AttributeOption.objects.create(
    group= color,
    option= 'Noir'
)
AttributeOption.objects.create(
    group= color,
    option= 'Blanc'
)


# optional feedback message

print ("AttributeOptionGroup & AttributeOption Added")