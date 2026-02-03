import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from myapp.models import Passcode

# Generate 10 initial passcodes
for _ in range(10):
    code = Passcode.generate_code()
    passcode, created = Passcode.objects.get_or_create(code=code)
    if created:
        print(f"Created passcode: {code}")
    else:
        print(f"Passcode {code} already exists")

print(f"\nTotal active passcodes: {Passcode.objects.filter(is_used=False).count()}")
print("\nActive passcodes:")
for p in Passcode.objects.filter(is_used=False):
    print(f"  {p.code}")
