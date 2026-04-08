from django.db import models

class Parcels(models.Model):
    # On définit les choix proprement
    class Status(models.IntegerChoices):
        REGISTERED = 1, 'Registered'
        SEND = 2, 'Send'
        RECEIVED = 3, 'Received'

    tracking_number = models.CharField(max_length=100, unique=True, blank=True)
    adr_dep = models.CharField(max_length=100)
    adr_arr = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=2) # Augmenté pour plus de sécurité
    status = models.IntegerField(choices=Status.choices, default=Status.REGISTERED)

    def __str__(self):
        # Utiliser tracking_number est souvent plus parlant que l'ID interne
        return f"Colis N°{self.id} - {self.weight}kg"

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            # On enregistre d'abord pour obtenir un ID
            super().save(*args, **kwargs)
            self.tracking_number = f"GN{self.id}"
            kwargs.pop('force_insert', None)  # Évite les erreurs lors du second save
            super().save(update_fields=['tracking_number'], *args, **kwargs)
        else:
            super().save(*args, **kwargs)