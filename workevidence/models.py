from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Worker(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    card_id = models.CharField(max_length=20,blank=True,null=True,unique=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name


class WorkEvidence(models.Model):
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    work_date = models.DateTimeField(blank=True, null=True)
 
    def __str__(self):
        return self.work_date

