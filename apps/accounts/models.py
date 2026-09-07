from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    USER_TYPES = (

        ("customer", "Customer"),

        ("owner", "Business Owner"),

    )


    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        default="customer"
    )


    def __str__(self):

        return self.user.username