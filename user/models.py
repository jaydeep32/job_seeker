from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='users', null=True, blank=True)
    is_company = models.BooleanField(default=False)
    address = models.TextField( null=True, blank=True)
    about = models.TextField( null=True, blank=True)
    resume = models.FileField(upload_to='resume', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, *args, **kwargs):
    if created:
        p = Profile(user=instance)
        p.save()




