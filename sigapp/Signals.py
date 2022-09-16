from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import User_profile,User
 
 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        User_profile.objects.create(user=instance)
  
