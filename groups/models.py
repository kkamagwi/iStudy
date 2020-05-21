from django.db import models
from django.utils import timezone


class Group(models.Model):
    short_name = models.CharField(max_length=15)
    cource = models.CharField(max_length=63)
    level = models.CharField(max_length=15)
    start_date = models.DateTimeField(default=timezone.now)
    payment_date = models.DateTimeField(default=timezone.now)
    next_payment_date = models.DateTimeField(default=timezone.now) #TODO function to count
    #TODO months since start
    teacher = models.CharField(max_length=127, default='guessing') #TODO foreign key

    def __str__(self):
        return self.short_name


