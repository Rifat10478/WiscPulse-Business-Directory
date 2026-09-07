from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        max_length=120,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Font Awesome icon class, e.g. fa-solid fa-utensils"
    )

    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "category_detail",
            kwargs={"slug": self.slug}
        )