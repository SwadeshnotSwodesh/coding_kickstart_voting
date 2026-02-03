import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from myapp.models import VotingPasscode

# Create or update the voting passcode
passcode_obj, created = VotingPasscode.objects.update_or_create(
    defaults={'passcode': 'admin123'}
)

if created:
    print(f"✓ Voting passcode created: {passcode_obj.passcode}")
else:
    print(f"✓ Voting passcode updated: {passcode_obj.passcode}")

print("\nThe admin can now enter this passcode repeatedly to allow each voter to vote.")
print("This same passcode is reused for all voters throughout the voting session.")
