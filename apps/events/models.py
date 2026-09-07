from django.db import models

class Event(models.Model):


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

 description = models.TextField()

 image = models.ImageField(
    upload_to="events/",
    blank=True,
    null=True
)

 location = models.CharField(
    max_length=255
)

 event_date = models.DateField()

 event_time = models.TimeField(
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

    ordering = [
        "event_date",
        "event_time",
    ]

    verbose_name = "Event"
    verbose_name_plural = "Events"

def __str__(self):

    return self.title

