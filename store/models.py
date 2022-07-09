from django.db import models

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Store(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="name"
                            )
    description = models.CharField(max_length=800,
                                   verbose_name="description"
                                   )
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)],
                                 verbose_name="rating"
                                 )

