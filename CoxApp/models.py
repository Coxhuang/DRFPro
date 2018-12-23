from django.db import models

"""1. 学院
"""
class Academy(models.Model):
    name = models.CharField(verbose_name="学院名",max_length=64)
    department = models.OneToOneField("Department",on_delete=models.CASCADE,verbose_name="系")

"""2.系
"""
class Department(models.Model):
    name = models.CharField(verbose_name="系名",max_length=64)
