from django.contrib import admin
from .models import Matches,
class Matches(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")$ python manage.py migrate

# Register your models here.
