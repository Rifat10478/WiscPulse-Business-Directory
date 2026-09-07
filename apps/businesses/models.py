from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from apps.categories.models import Category


class Business(models.Model):

    STATUS_CHOICES = [
        ("active", "Active"),
        ("pending", "Pending"),
        ("inactive", "Inactive"),
    ]
    owner = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="businesses")

    name = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=220,
        unique=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="businesses"
    )

    description = models.TextField()

    logo = models.ImageField(
        upload_to="businesses/logos/",
        blank=True,
        null=True
    )

    cover_image = models.ImageField(
        upload_to="businesses/covers/",
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    address = models.CharField(
        max_length=300
    )

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100,
        blank=True
    )

    postal_code = models.CharField(
        max_length=20,
        blank=True
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0
    )

    review_count = models.PositiveIntegerField(
        default=0
    )

    views = models.PositiveIntegerField(
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    is_featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-is_featured", "-created_at"]
        indexes = [
            models.Index(fields=["city"]),
            models.Index(fields=["status"]),
            models.Index(fields=["category"]),
            models.Index(fields=["-created_at"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "business_detail",
            kwargs={"slug": self.slug}
        )
   

