from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    description = models.TextField()
    image =  models.ImageField(blank=True)
    
    def __str__(self):
        return self.title
    
    @classmethod
    def search_by_category(cls,search_term):
        posts = cls.objects.filter(category__name__icontains=search_term)
        return posts
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, default = None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/',default = 'default.jpg')

    def __str__(self):
        return self.post.title






