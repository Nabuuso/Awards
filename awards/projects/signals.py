from django.db.models.signals import post_save
from django.dispatch import receiver
from projects.models import Rating

@receiver(post_save,sender=Rating)
def rating_handler(sender,instance,created,*args,**kwargs):
    pass