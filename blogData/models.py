from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.caption}" 

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)
    def __str__(self):
        return f"{self.first_name}, ({self.last_name})" 

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="updates/", blank=True, null=True)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return f"{self.title}, ({self.date}), ({self.author})" 

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    text = models.TextField(validators=[MinLengthValidator(5)])
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Comentario de {self.name} en {self.post}"
