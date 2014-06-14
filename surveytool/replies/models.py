from django.db import models

class Answer(models.Model):
    farmer_id = models.CharField(max_length=50)
    phone_number = models.CharField(max_length = 11)
    question_id = models.IntegerField(default=0)
    date = models.DateTimeField('date answered')
    answer = models.CharField(max_length=200)
