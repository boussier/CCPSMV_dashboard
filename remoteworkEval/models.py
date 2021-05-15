from django.db import models
from django.utils import timezone
from users.models import CustomUser

class RemoteworkEval(models.Model):
    class Meta:
        verbose_name = "Evaluation période de télétravail"   
        verbose_name_plural = "Evaluations période de télétravail"

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name="utilisateur")
    date = models.DateField(default=timezone.now())
    mail = models.IntegerField('Courrier', null=True, blank=True)
    archiving = models.IntegerField('Archivage', null=True, blank=True)
    instruction = models.IntegerField('Instruction', null=True, blank=True)
    filesFollowUp = models.IntegerField('Suivi dossiers', null=True, blank=True)
    meetingPreparation = models.IntegerField('Préparation réunion ou compte rendu', null=True, blank=True)
    others = models.IntegerField('Autres', null=True, blank=True)            

    def __str__(self):
        return '%s' % (self.id)
