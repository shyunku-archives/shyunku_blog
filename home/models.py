from django.db import models

# Create your models here.


class User_Info(models.Model):
    user_id = models.CharField(max_length=20)
    user_nickname = models.CharField(max_length=25)
    user_pw = models.CharField(max_length=15)

    def __str__(self):
        return self.user_id


class Variables(models.Model):
    visits = models.IntegerField(default=0)
    doc_index_recent = models.IntegerField(default=1)

    def __str__(self):
        return "Variables"

class Documents_Info(models.Model):
    classify = models.CharField(max_length=20)
    doc_index = models.CharField(default="0000001", max_length=15)
    doc_title = models.CharField(max_length=20)
    doc_writer = models.CharField(default="shyunku", max_length=20)
    doc_time = models.TimeField()
    doc_view_cnt = models.IntegerField(default=0)

    def __str__(self):
        return self.classify + "-" + self.doc_index