from django.db import models
from django.utils import timezone
from django.conf import settings
from students.models import Student


class Payment(models.Model):
    date = models.DateTimeField(default=timezone.now)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.FloatField(default=1500)
    month = models.IntegerField(default=1)  # TODO count itself
    admin = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)

    def __str__(self):
        date = str(self.date)
        return date[:10]
