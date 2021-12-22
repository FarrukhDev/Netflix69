from django.db import models

class Actor(models.Model):
    name=models.CharField(max_length=20)
    birth_date=models.DateField()
    gender=models.CharField(max_length=10)
    def __str__(self):
        return self.name
class Movie(models.Model):
    title=models.CharField(max_length=50)
    genre=models.CharField(max_length=15,choices=(('horror','horror'),('ficsion','ficsion'),('milodram','milodram')))
    date=models.DateField()
    actors=models.ManyToManyField(Actor)
    def __str__(self):
        return self.title
