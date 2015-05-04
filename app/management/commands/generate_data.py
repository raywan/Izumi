import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from api.models import Source, History
from app.models import IzumiUser

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _generate_sources(self):
        for i in range(10):
            lat = random.randint(-90, 90) + round(random.random(), 6)
            lng = random.randint(-180, 180) + round(random.random(), 6)
            source_type = random.choice(["surface", "ground", "frozen", "other"])
            source_health = random.randint(0, 100)
            pathogen_pollution =  random.randint(0,100)
            inorganic_pollution = random.randint(0,100)
            organic_pollution = random.randint(0,100)
            macroscopic_pollution = random.randint(0,100)
            thermal_pollution =  random.randint(0,100)
            climate_condition = random.randint(0,100)
            depletion_risk = random.randint(0,100)
            stress =  random.randint(0,100)

            new_source = Source(
                author = random.choice(IzumiUser.objects.all()),
                date_created = timezone.now(),
                last_updated = timezone.now(),
                latitude=lat,
                longitude=lng,
                source_type=source_type,
                pathogen_pollution = pathogen_pollution,
                inorganic_pollution = inorganic_pollution,
                organic_pollution = organic_pollution,
                macroscopic_pollution = macroscopic_pollution,
                thermal_pollution = thermal_pollution,
                climate_condition = climate_condition,
                depletion_risk = depletion_risk,
                stress =  stress
                )
            new_source.save()

    def handle(self, *args, **options):
        self._generate_sources()
