from django.db import models
from products.models import Product
from profiles.models import UserProfile
from django.conf import settings


class Wishlist(models.Model):
    user = models.ForeignKey(
                             settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE
                             )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} whish list'
