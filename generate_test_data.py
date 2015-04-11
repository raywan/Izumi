import random
from django.contrib.auth.models import User
from api.models import Source, Event
from app.models import IzumiUser
from django.utils import timezone

def generate_users(num):
    for i in range(num):
        new_user = User.objects.create_user(
            username=
            email=
            first_name=
            last_name=
            password=
        )
        new_izumi_user = IzumiUser(
            user=new_user,
            organization=form.cleaned_data.get('organization'),
        )
        new_izumi_user.save()

def generate_sources(num):
    for i in range(num):
        lat = random.randint(-90, 90) + round(random.random(), 6)
        lng = random.randint(-180, 180) + round(random.random(), 6)
        source_type = random.choice(["surface", "ground", "frozen", "other"])
        source_health = random.randint(0, 100)
        pathogen_pollution =  random.randint(0,100)
        inorganic_pollution = random.randint(0,100)
        organic_pollution = random.randint(0,100)
        macroscopic_pollution = random.randint(0,100)
        thermal_pollution =  random.randint(0,100)
        new_source = Source(
            author =
            date_created = timezone.now()
            last_update = timezone.now()
            latitude=lat,
            longitude=lng,
            source_type=source_type,
            pathogen_pollution = pathogen_pollution
            inorganic_pollution = inorganic_pollution
            organic_pollution = organic_pollution
            macroscopic_pollution = macroscopic_pollution
            thermal_pollution = thermal_pollution
            )

def generate_events(num):
    pass
