import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from myapp.models import Team

# Create sample teams for each category
scratch_teams = ['Team Alpha', 'Team Beta', 'Team Gamma', 'Team Delta', 'Team Epsilon', 'Team Zeta']
app_inventor_teams = ['App Squad One', 'App Squad Two', 'App Squad Three', 'App Squad Four', 'App Squad Five', 'App Squad Six']
robotics_teams = ['Robot Legends', 'Robot Masters', 'Robot Innovators', 'Robot Experts', 'Robot Champions', 'Robot Titans']

for name in scratch_teams:
    Team.objects.get_or_create(name=name, category='scratch')

for name in app_inventor_teams:
    Team.objects.get_or_create(name=name, category='app_inventor')

for name in robotics_teams:
    Team.objects.get_or_create(name=name, category='robotics')

print("Sample teams created successfully!")
print(f"Total teams: {Team.objects.count()}")
