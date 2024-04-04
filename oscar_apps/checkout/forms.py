from oscar.apps.checkout.forms import ShippingAddressForm as CoreShippingAddressForm
from oscar.core.loading import get_class, get_model
Country = get_model("address", "Country")


class ShippingAddressForm(CoreShippingAddressForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.adjust_country_field()

    def adjust_country_field(self):
        # countries = Country._default_manager.filter(is_shipping_country=True)
        countries = Country._default_manager.filter(printable_name='Senegal')
        
        # No need to show country dropdown if there is only one option
        if len(countries) == 1:
            self.fields.pop("country", None)
            self.instance.country = countries[0]
        else:
            self.fields["country"].queryset = countries
            self.fields["country"].empty_label = None

    class Meta:
        model = get_model("order", "shippingaddress")
        fields = [
            "first_name",
            "last_name",
            "line1",
            "line2",
            "line3",
            "line4",
            "state",
            "postcode",
            "country",
            "phone_number",
            "notes",
        ]

