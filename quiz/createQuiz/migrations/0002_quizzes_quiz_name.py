# Generated by Django 2.2.4 on 2019-08-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createQuiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizzes',
            name='quiz_name',
            field=models.CharField(default='quiz', max_length=50),
            preserve_default=False,
        ),
    ]
