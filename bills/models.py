from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Bills(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    dueDate = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ]
     )
    automaticPayment = models.BooleanField(null=True,)
    payd = models.BooleanField(null=True,) # default false
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name