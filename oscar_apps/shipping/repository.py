from oscar.apps.shipping import methods
from oscar.apps.shipping.repository import Repository as CoreRepository
from decimal import Decimal as D
from oscar.core.loading import get_classes

(
    Free,
    NoShippingRequired,
    TaxExclusiveOfferDiscount,
    TaxInclusiveOfferDiscount,
) = get_classes(
    "shipping.methods",
    [
        "Free",
        "NoShippingRequired",
        "TaxExclusiveOfferDiscount",
        "TaxInclusiveOfferDiscount",
    ],
)


#Specifier le cout de la livraison (fixe)
class Standard(methods.FixedPrice):
    code = 'standard'
    name = 'Standard shipping'
    charge_excl_tax = D('5000.00')
    charge_incl_tax = D('5000.00')



class Repository(CoreRepository):

    methods = (Free(), Standard())


