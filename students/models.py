from django.db import models
from django.utils import timezone
from groups.models import Group


class Reason(models.Model):
    REASONS_CHOISES=(('денег нету','денег нету длинный шмель'),
                       ('всё узнал','всё знаю!') )
    name= models.CharField(max_length=200,choices=REASONS_CHOISES,default='денег нету')
    
    def __str__(self):
        return self.name

        
class Student(models.Model):
    surname = models.CharField(max_length=127)
    name = models.CharField(max_length=127)
    group = models.ForeignKey(Group, on_delete=models.CASCADE) #TODO many-to-many
    active = models.BooleanField()
    admission_date = models.DateTimeField(default=timezone.now)
    reason = models.OneToOneField(Reason,on_delete=models.CASCADE,primary_key=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.surname





class Nomenclature(models.Model):
    UNIT_CHOICES=(
        ('шт','шт'),
        ('час','час')
    )
    
    NOMENCLATURE_TYPES=(
        ('услуга','услуга'),
        ('товар','товар')
    )

    title= models.CharField(max_length=250)
    unit= models.CharField(max_length=20,choices=UNIT_CHOICES,default='час')
    type_of_nomenclature= models.CharField(max_length=20,choices=NOMENCLATURE_TYPES,default='час')
    notes = models.CharField(max_length=255, blank=True, null=True)

