import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


def get_photo_upload_path(instance, filename):
	return os.path.join("user-photos/", filename)

class CustomUser(AbstractUser):
    weight = models.PositiveIntegerField( default=0, blank=True)
    age = models.PositiveIntegerField(default=0, blank=True)
    height = models.PositiveIntegerField(default=0, blank=True)
    photo = models.ImageField(upload_to=get_photo_upload_path, blank=True)

# Generate random username while creating new user
def random_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = uuid.uuid4().hex[:30]


models.signals.pre_save.connect(random_username, sender=settings.AUTH_USER_MODEL)
