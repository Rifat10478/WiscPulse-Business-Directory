from django.db import models

from django.contrib.auth.models import User

from apps.businesses.models import Business



class Review(models.Model):

    RATING_CHOICES = [

        (1, "★"),
        (2, "★★"),
        (3, "★★★"),
        (4, "★★★★"),
        (5, "★★★★★"),

    ]


    business = models.ForeignKey(

        Business,

        on_delete=models.CASCADE,

        related_name="reviews"

    )


    user = models.ForeignKey(

        User,

        on_delete=models.CASCADE

    )


    rating = models.PositiveIntegerField(

        choices=RATING_CHOICES

    )


    comment = models.TextField()


    created_at = models.DateTimeField(

        auto_now_add=True

    )


    class Meta:

        ordering = [

            "-created_at"

        ]



    def __str__(self):

        return f"{self.business.name} - {self.rating}"