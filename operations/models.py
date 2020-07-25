from django.db import models
from django.utils import timezone


class Operation(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class OperationsJournal(models.Model):
    operation = models.OneToOneField(Operation, on_delete=models.CASCADE)
    date_of_operation = models.DateTimeField(default=timezone.now)
