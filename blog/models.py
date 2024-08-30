from django.urls import reverse
from django.utils import timezone
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name



class ChopetishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Chopetish)

class News(models.Model):

    class Status(models.TextChoices):
        Qoralama = "QR", "Qoralama"
        Chopetish = "CHP", "Chopetish"

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    body = models.TextField()
    image = models.ImageField(upload_to="News/images")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3,
                              choices=Status.choices,
                              default=Status.Qoralama)
    objects = models.Manager()
    chopetish = ChopetishManager()

    class Meta:
        ordering = ["-publish_time"]

    def get_absolute_url(self):
        return reverse("detali", args=[self.slug])

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    xabar = models.TextField()

    def __str__(self):
        return self.name




