from django.db import models


# Create your models here.

class quiz(models.Model) :
    quiz_index = models.IntegerField()
    quiz_string = models.CharField()

