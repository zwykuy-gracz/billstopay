from django.db import models


class Bills(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    payd = models.BooleanField() # default false
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name