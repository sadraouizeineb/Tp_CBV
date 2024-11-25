# view/models.py
from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    bio = models.TextField(blank=True, null=True)  # Biographie optionnelle

    def __str__(self):
        return self.bio

# class BlogPost(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Lié au modèle `Author`
#     created_on = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title



class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Lié au modèle `Author`
    created_on = models.DateTimeField(blank=True, null=True)  # Modifiable et optionnel

    def __str__(self):
        return self.title
