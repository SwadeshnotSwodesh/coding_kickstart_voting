import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User

user = User.objects.get(username='admin')
user.set_password('password123')
user.save()
print("Admin password set to: password123")
