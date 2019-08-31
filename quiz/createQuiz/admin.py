from django.contrib import admin
from createQuiz.models import quizzes
from takeQuiz.models import taken_quiz
# Register your models here.

admin.site.register(quizzes)
admin.site.register(taken_quiz)
