from oscar.apps.order.utils import OrderDispatcher as CoreOrderDispatcher
from django.core.mail import mail_admins


class OrderDispatcher(CoreOrderDispatcher):

    def send_order_placed_email_for_user(self, order, extra_context, attachments=None):
        event_code = self.ORDER_PLACED_EVENT_CODE
        messages = self.dispatcher.get_messages(event_code, extra_context)
        subject = f"Nouvelle Commande recue: Order #{order.number}"
        message = f"Une commande à été faite par : \n Client : {order.shipping_address.first_name} {order.shipping_address.last_name}\n Tel : {order.shipping_address.phone_number} "
        mail_admins(subject, message)
        self.dispatch_order_messages(
            order, messages, event_code, attachments=attachments
        )