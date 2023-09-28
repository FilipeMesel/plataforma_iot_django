from django.db import models

# Create your models here.

from django.db import models

class DispositivoIoT(models.Model):
    id = models.AutoField(primary_key=True)
    serialNumber = models.CharField(max_length=255)
    dados = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dispositivo IoT - ID: {self.id}, Serial Number: {self.serialNumber}"

