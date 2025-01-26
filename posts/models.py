from django.db import models
from authors.models import Author
from authors.base_model import BaseModel
from tags.models import Tag
from catalogs.models import Catalog


class Post(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Post Title")
    content = models.TextField(verbose_name="Content")
    img = models.ImageField(upload_to='posts/', verbose_name="Post Picture")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts", verbose_name="Author")
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="posts", verbose_name="Catalog")
    tags = models.ManyToManyField(Tag, related_name="tags", verbose_name="Tags")
    views = models.PositiveIntegerField(default=0, verbose_name="View Count")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", verbose_name="Post")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="comments", verbose_name="Author")
    content = models.TextField(verbose_name="Comment Content")
    email = models.EmailField(verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"


    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['-created_at']