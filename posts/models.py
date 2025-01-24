from django.db import models
from authors.models import Author
from authors.base_model import BaseModel
from tags.models import Tag
from catalogs.models import Catalog


class Post(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Post Title")
    content = models.TextField(verbose_name="Content")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts", verbose_name="Author")
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="posts", verbose_name="Catalog")
    tags = models.ManyToManyField(Tag, related_name="tags", verbose_name="Tags")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
