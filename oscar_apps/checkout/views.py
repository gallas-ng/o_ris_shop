from django.shortcuts import redirect
from django.urls import reverse
from oscar.apps.checkout import views

class PaymentMethodView(views.PaymentMethodView):

    def form_valid(self, form):
        """
        redirect to preview if payment_method == cash-on-delivery
        """
        payment_method = form.cleaned_data["payment_method"]
        self.checkout_session.pay_by(payment_method.code)
        if payment_method.code == 'cash-on-delivery':
            return redirect(reverse("checkout:preview"))
        return super().form_valid(form)