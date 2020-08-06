from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import CustomerModel

def CustomerDetails(sender, instance, created, **kwargs):
	if created:
                group=Group.objects.get(name='customer')
                instance.groups.add(group)
                CustomerModel.objects.create(
                        user=instance,
                        name=instance.username,
                        )
                print('Profile created!')

post_save.connect(CustomerDetails, sender=User)
