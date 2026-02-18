from django.db import models

# Create your models here.
#Model of a user where it takes age and name of the user
class AppUser(models.Model):
    age = models.IntegerField(default=0)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
 