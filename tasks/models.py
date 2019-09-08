from django.db import models

# Create your models here.


class Task(models.Model):
    text = models.CharField(max_length=255)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.text
