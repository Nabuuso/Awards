from django.db.models.signals import post_save
from django.dispatch import receiver
from projects.models import Rating,Project

@receiver(post_save,sender=Rating)
def rating_handler(sender,instance,created,*args,**kwargs):
    project = Project.objects.get(pk=instance.project.id)
    project.design_rating += int(instance.design_rating)
    project.content_rating += int(instance.content_rating)
    project.usability_rating += int(instance.usability_rating)
    project.total_raters += 1
    project.save()