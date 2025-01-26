from django.db import models
from authors.base_model import BaseModel
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from datetime import date


class Author(BaseModel):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    bio = models.TextField(blank=True, null=True, verbose_name="Biography")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Birth Date")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL Slug")
    profile_picture = models.ImageField(upload_to='authors/', blank=True, null=True, verbose_name="Profile Picture")
    is_active = models.BooleanField(default=False)

    def clean(self):
        if self.birth_date and self.birth_date > date.today():
            raise ValidationError("Birth date cannot be in the future.")

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.first_name}-{self.last_name}")
            slug = base_slug
            count = 1
            while Author.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.birth_date})"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        unique_together = ('first_name', 'last_name')
