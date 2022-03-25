from django.db import models
from django.contrib.auth.models import User


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    attributes = models.JSONField(default=dict, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.display_name} ({self.name})"


class Release(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.display_name} ({self.name})"


def upload_file_products(instance, filename):
    return f"{filename}"


class Product(models.Model):
    display_name = models.CharField(max_length=255)
    # product_dir = models.CharField(max_length=255)
    main_file = models.FileField(
        upload_to=upload_file_products, null=False, blank=False
    )
    file_name = models.CharField(max_length=120)
    file_size = models.IntegerField()
    file_extension = models.CharField(max_length=10)
    description_file = models.FileField(
        upload_to=upload_file_products, null=True, blank=True
    )
    official_product = models.BooleanField(default=False)
    survey = models.CharField(max_length=255, null=True, blank=True)
    pz_code = models.CharField(max_length=55, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="products"
    )
    product_type = models.ForeignKey(
        ProductType, on_delete=models.PROTECT, related_name="products"
    )
    release = models.ForeignKey(
        Release,
        on_delete=models.PROTECT,
        related_name="products",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.display_name} ({self.file_name})"
