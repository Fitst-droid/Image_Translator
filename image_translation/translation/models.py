from django.db import models

class Image(models.Model):
  Name = models.CharField(max_length=255, unique=True)
  image = models.ImageField(uoload_to='images/')

  def __str__(self):
    return self.Name

# Create your models here.
