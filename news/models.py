from django.db import models
from ckeditor.fields import RichTextField
from category.models import Category


# Create your models here.
class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=500)

    image = models.ImageField(upload_to='news')

    short_description = models.TextField(null=True, blank=True)

    description = RichTextField()

    tags = models.CharField(max_length=500, null=True, blank=True)

    views = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
