from django.db import models
from datetime import time
from django.utils import timezone

class Worker(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    card_id = models.CharField(max_length=20,blank=True,null=True,unique=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class WorkEvidence(models.Model):
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    @property
    def all_time(self):
        return self.end_date - self.start_date


    def __str__(self):
        return f'{self.id}'

