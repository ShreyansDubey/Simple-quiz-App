from django.db import models

# Create your models here.

class taken_quiz(models.Model) :
    user = models.CharField(max_length=50)
    quiz_taken_JSON = models.CharField(max_length=3000)

    def __str__(self) :
        return (str(self.user) + str(self.quiz_taken_JSON))
    

