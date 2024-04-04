from oscar.core.loading import get_model
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ris.settings.dev")
import django
django.setup()

from django.contrib.auth.models import User

# Create a new superuser
username = 'gallas'
password = 'Dorwar@222'
email = 'fniang89@gmail.com'

# Get or create the superuser
user, created = User.objects.get_or_create(username=username, email=email)
if created:
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print('Superuser created.')
else:
    print('Superuser already exists.')


# Create cash on delivery payment method
SourceType = get_model('payment', 'SourceType')
SourceType.objects.get_or_create(name='Cash on delivery')