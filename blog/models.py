import datetime

from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def author(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.author()


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)

    # def save(self, *args, **kwargs):
    #     if self.date > datetime.datetime.now():
    #         raise ValueError("Date can't be in the future")
    #
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def book(self):
        return f"{self.title}, ({self.author})"

    def __str__(self):
        return self.book()
