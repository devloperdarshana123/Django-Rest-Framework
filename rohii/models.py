from django.db import models

class Rohii(models.Model):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):  # Fixed method definition
        return self.name

# Create your models here.
