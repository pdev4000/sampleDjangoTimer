from audioop import reverse
from django.db import models
from django.urls import reverse

# Create your models here.
class exam (models.Model) :
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url (self):
        return reverse('tests:home',kwargs={id :'self.id'})

class section (models.Model) :
    test = models.ForeignKey(exam, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    time = models.IntegerField()
    order = models.IntegerField()
    questions = models.IntegerField()

    def __str__(self):
        return self.section

