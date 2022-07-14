from django.db import models

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Store(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="name")
    description = models.CharField(max_length=800,
                                   verbose_name="description")
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)],
                                 verbose_name="rating")
    owner = models.ForeignKey("auth.User",
                              on_delete=models.SET_NULL,
                              related_name='stores',
                              null=True,
                              blank=True)
    status = models.CharField(choices=(("in_review", "In Review"),
                                       ("active", "Active"),
                                       ("deactivated", "Deactivated")),
                              default="in_review",
                              max_length=15)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'Store: {self.name}, Owner: {self.owner}'
