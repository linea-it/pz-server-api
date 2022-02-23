from django.db import models
from django.contrib.auth.models import User


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    attributes = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.display_name} ({self.name})'


def upload_file_products(instance, filename):
    return f'{instance.product_id}-{filename}'


class Product(models.Model):
    display_name = models.CharField(max_length=255)
    product_dir = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name='products')
    file_name = models.CharField(max_length=120)
    main_file = models.FileField(upload_to=upload_file_products, null=False, blank=False)
    file_size = models.IntegerField()
    file_extension = models.CharField(max_length=10)
    official_product = models.BooleanField(default=False)
    survey = models.CharField(max_length=255)
    pz_code = models.CharField(max_length=55)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='products')
    
    def __str__(self):
        return f'{self.display_name} ({self.file_name})'