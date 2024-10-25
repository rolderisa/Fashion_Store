from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Category


# Create your models here.
class CustomerPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.CharField(max_length=20, blank=True)
    color = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.username}'s preferences"

@receiver(post_save, sender=User)
def create_or_update_customer_preference(sender, instance, created, **kwargs):
    if created:
        CustomerPreference.objects.create(user=instance)
    else:
        instance.customerpreference.save()
