from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    def url(self):
        return f"/author/{self.id}"



class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()
    favorited_by = models.ManyToManyField(
        Author,
        symmetrical=False,
        blank=True,
        related_name='favorites'
    )

    def __str__(self):
        return self.title
    def url(self):
        return f"/recipe/{self.id}"

