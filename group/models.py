import random
import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver 

# from user.models import Teacher


class Room(models.Model):
    room = models.CharField(max_length=30, verbose_name='Xona nomi')

    def __str__(self):
        return self.room


class Vaqt(models.Model):
    vaqt = models.CharField(max_length=35)

    def __str__(self):
        return self.vaqt

class Subject(models.Model):
    name = models.CharField(max_length=125)
    fee = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Group(models.Model):
    
    PAYT = (
        ('du/chor/ju', 'du/chor/ju'),
        ('se/pay/shanba', 'se/pay/shanba')
    )

    name = models.CharField(max_length=190, null=True, blank=True)
    payt = models.CharField(choices=PAYT, default='du/chor/ju', max_length=25)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='xona', related_name='guruhlar')
    vaqt = models.ForeignKey(Vaqt, on_delete=models.CASCADE, verbose_name='vaqt', related_name='guruhlar')
    teacher = models.ForeignKey("user.Teacher", on_delete=models.CASCADE, verbose_name='Ustoz', related_name='guruhlar')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Fan', related_name='guruhlar')

    def __str__(self):
        return f'{self.name}-{self.subject}'

@receiver(pre_save, sender=Group)
def create_group_name(sender, instance, created, **kwargs):
    if not instance.id:
        s = ""
        r = uuid.uuid4().hex[:6].upper()
        if " " in str(instance.subject.name):
            for i in str(instance.subject.name).split():
                s += i[0].upper()
        else:    
            s = str(instance.subject.name)[:2].upper()
        instance.name = s + "-" + str(r)
        instance.save()

