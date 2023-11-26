from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from group.models import Group, Subject


class User(AbstractUser):
    STATUS = (
        ('Manager', 'Manager'),
        ('Boshqaruvchi', 'Boshqaruvchi'),
        ('Ustoz', 'Ustoz'),
        ('O\'quvchi', 'O\'quvchi')
    )

    GENDER = (
        ('erkak', 'erkak'),
        ('ayol', 'ayol')
    )

    status = models.CharField(max_length=25, choices=STATUS, default='O\'quvchi', verbose_name='Status')
    photo = models.ImageField(upload_to='UserPhotos/', default='UserPhotos/user.png', verbose_name='Profil rasm')
    gender = models.CharField(max_length=25, choices=GENDER, default='erkak', verbose_name='Jinsi')
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Tel raqam')

    def __str__(self):
        return f'{self.first_name}, {self.last_name} - {self.status}'


@receiver(post_save, sender = User)
def create_user(sender, instance, created, **kwargs):
    if created:
        if instance.gender == 'ayol':
            instance.photo='UserPhotos/woman.png'
            instance.save()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Ustoz')
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.user


class Chegirma(models.Model):
    protsent = models.PositiveIntegerField(default=0)
    reason = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.protsent


class Pupil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='pupils')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='guruh', related_name='pupils')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default=True)
    comment = models.CharField(max_length=300, blank=True, null=True)
    transfer_to_group = models.TextField(verbose_name='Guruh almashtirish sababi')
    chegirma = models.ForeignKey(Chegirma, on_delete=models.CASCADE, null=True, blank=True, related_name='pupils', verbose_name='chegirma')

    def __str__(self):
        return F'{self.user} - {self.chegirma} chegirmali'
