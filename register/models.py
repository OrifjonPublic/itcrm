from django.db import models
from group.models import Subject, Vaqt


class Xabardorlik(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Royhat(models.Model):
    
    PAYT = (
        ('du/chor/ju', 'du/chor/ju'),
        ('se/pay/shanba', 'se/pay/shanba')
    )
    
    first_name = models.CharField(max_length=50, verbose_name='Ism', null=True, blank=True)
    last_name = models.CharField(max_length=50, verbose_name='Familiya', null=True, blank=True)
    phone_number_1 = models.CharField(max_length=20, verbose_name='Asosiy Tel raqam', null=True, blank=True)
    phone_number_2 = models.CharField(max_length=20, verbose_name='Qo\'shimcha Tel raqam', null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='list')
    xabardor = models.ForeignKey(Xabardorlik, on_delete=models.CASCADE, related_name='list', null=True, blank=True)
    payt = models.CharField(choices=PAYT, default='du/chor/ju', max_length=25)
    comment = models.CharField(max_length=300, blank=True, null=True)
    vaqt = models.ForeignKey(Vaqt, on_delete=models.CASCADE, verbose_name='vaqt', related_name='list', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name} - {self.subject}'
