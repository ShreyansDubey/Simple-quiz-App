from django.db import models


# Create your models here.


#holds basic quiz details; questions, options and answers
class quizzes(models.Model) :
    quiz_index = models.IntegerField()
    quiz_string = models.CharField(max_length=3000)
    quiz_name = models.CharField(max_length=50)
    times_attempted = models.IntegerField(default=0)

    def __str__(self) :
        return str(self.quiz_index)
