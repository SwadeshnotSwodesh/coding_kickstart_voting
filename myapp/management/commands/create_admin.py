from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Create superuser if it does not exist"

    def handle(self, *args, **options):
        User = get_user_model()

        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not email or not password:
            self.stdout.write(self.style.WARNING(
                "Superuser env vars not set"
            ))
            return

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.SUCCESS(
                "Superuser already exists"
            ))
            return

        User.objects.create_superuser(
            email=email,
            password=password
        )

        self.stdout.write(self.style.SUCCESS(
            "Superuser created successfully"
        ))
