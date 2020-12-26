from django.db import models

class Destinations(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    review = models.TextField()
    review2 = models.TextField()
    offer = models.BooleanField(default=False)

