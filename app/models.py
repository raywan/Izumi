from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class IzumiUser(models.Model):
    user = models.OneToOneField(User)
    organization = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user.get_username()
