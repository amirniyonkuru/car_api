from django.db import models


class Rating(models.Model):
    rate_num = models.IntegerField(default=0)

    def __str__(self):
        return str(self.rate_num)


class Car(models.Model):
    carmodel = models.CharField(max_length=100, null=True)
    carmake = models.CharField(max_length=100, null=True)
    rating = models.ManyToManyField(Rating, default=0)

    def __str__(self):
        return f"{self.carmake} {self.carmodel}"
