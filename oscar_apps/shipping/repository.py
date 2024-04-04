from oscar.apps.shipping import methods
from oscar.apps.shipping.repository import Repository as CoreRepository
from decimal import Decimal as D
from oscar.core.loading import get_classes
from django.template.loader import render_to_string
from oscar.core import prices

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

class charge_per_item(methods.Base):
    code = 'standard_2'
    name = 'Livraison Standard'

    charge_per_item = D('1500.00')
    threshold = D('100000.00')

    def calculate(self, basket):
        # Free for orders over some threshold
        if basket.total_incl_tax > self.threshold:
            return prices.Price(
                currency=basket.currency,
                excl_tax=D('0.00'),
                incl_tax=D('0.00'))

        # Simple method - charge 1500 per item
        total = basket.num_items * self.charge_per_item
        return prices.Price(
            currency=basket.currency,
            excl_tax=total,
            incl_tax=total)


class self_pick_up(methods.NoShippingRequired):

    code = 'no_shipping'
    name = 'Recuperer sur place'

class Repository(CoreRepository):

    methods = (charge_per_item(), self_pick_up)


