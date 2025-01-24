from django.db import models
from authors.base_model import BaseModel


class Catalog(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Catalog Name")
    desc = models.TextField(blank=True, null=True, verbose_name="Description")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL Slug")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.name.lower().replace(" ", "-")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Catalog"
        verbose_name_plural = "Catalogs"
