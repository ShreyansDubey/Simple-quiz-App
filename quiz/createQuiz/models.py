from django.db import models


# Create your models here.

class quizzes(models.Model) :
    quiz_index = models.IntegerField()
    quiz_string = models.CharField(max_length=3000)

    def __str__(self) :
        return str(self.quiz_index)

