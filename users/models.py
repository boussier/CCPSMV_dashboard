import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
import os
from django.core.validators import MaxValueValidator, MinValueValidator


class TimeWindow(models.Model):
    class Meta:
        verbose_name = "Fenêtre de temps"
        
    name = models.CharField('Nom', max_length=250, default='', null=True, blank=True)

    def __str__(self):
        return '%s' % (self.name)
    

class VehicleType(models.Model):
    class Meta:
        verbose_name = "Type de véhicule"

    name = models.CharField('Nom', max_length=250,default='', null=True, blank=True)

    def __str__(self):
        return '%s' % (self.name)


def get_photo_upload_path(instance, filename):
	return os.path.join("user-photos/", filename)


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "Utilisateur"
    age = models.PositiveIntegerField(default=0, blank=True)
    weight = models.PositiveIntegerField(default=0, blank=True)
    height = models.PositiveIntegerField(default=0, blank=True)
    distanceToWork = models.IntegerField('Distance travail domicile (km)', null=True, blank=True)
    travelDuration = models.IntegerField('Durée du trajet (en mn)', null=True, blank=True)
    averageCosumption = models.FloatField('Consommation moyenne (l/100km)', null=True, blank=True)
    vehicleType = models.ForeignKey(VehicleType, on_delete=models.CASCADE, verbose_name="Type de véhicule", null=True, blank=True)
    agendaRemoteWorking = models.ManyToManyField(TimeWindow,  verbose_name="Agenda télétravail")
    notation = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)]
    )


    photo = models.ImageField(upload_to=get_photo_upload_path, blank=True)

# Generate random username while creating new user
def random_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = uuid.uuid4().hex[:30]


models.signals.pre_save.connect(random_username, sender=settings.AUTH_USER_MODEL)

