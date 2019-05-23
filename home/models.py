from django.db import models

# Create your models here.


class User_Info(models.Model):
    user_id = models.CharField(max_length=15)
    user_nickname = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=15)

    def __str__(self):
        return self.user_id