from django.db import models
from django.utils import timezone
from groups.models import Group


class Student(models.Model):
    surname = models.CharField(max_length=127)
    name = models.CharField(max_length=127)
    group = models.ForeignKey(Group, on_delete=models.CASCADE) #TODO many-to-many
    # active = models.BinaryField(default=True)
    admission_date = models.DateTimeField(default=timezone.now)
    notes = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.surname
