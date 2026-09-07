from django.db import models

class News(models.Model):


 STATUS_CHOICES = (
    ("draft", "Draft"),
    ("published", "Published"),
)

 title = models.CharField(
    max_length=200
)

 slug = models.SlugField(
    unique=True
)

 short_description = models.CharField(
    max_length=300
)

 content = models.TextField()

 image = models.ImageField(
    upload_to="news/",
    blank=True,
    null=True
)

 status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default="draft"
)

 created_at = models.DateTimeField(
    auto_now_add=True
)

 updated_at = models.DateTimeField(
    auto_now=True
)

class Meta:

    ordering = ["-created_at"]

    verbose_name = "News"
    verbose_name_plural = "News"

def __str__(self):

    return self.title

