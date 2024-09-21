from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(
        default=0,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("newspaper:redactors-detail", args=[str(self.id)])


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="newspapers"
    )
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="newspapers"
    )

    def display_authors(self):
        return ', '.join([author.username for author in self.publishers.all()])

    display_authors.short_description = 'Authors'

    class Meta:
        ordering = ("-published_date",)

    def __str__(self):
        return f"{self.topic} {self.title}"

    def get_absolute_url(self):
        return reverse("newspaper:newspaper-detail", args=[str(self.id)])
