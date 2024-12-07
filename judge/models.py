from django.db import models
from performer.models import Performer

class Judge(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Audition(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Performance(models.Model):
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
    audition = models.ForeignKey(Audition, on_delete=models.CASCADE)
    score = models.PositiveIntegerField() 

    def __str__(self):
        return f"{self.performer} in {self.audition}"
