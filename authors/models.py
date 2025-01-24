from django.db import models
from authors.base_model import BaseModel
from django.utils.text import slugify


class Author(BaseModel):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    bio = models.TextField(blank=True, null=True, verbose_name="Biography")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Birth Date")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL Slug")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
