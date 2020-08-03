from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update_category()
    
class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.update_location()
    
    @classmethod
    def get_location(cls):
        location = cls.objects.all()
        return location


class Post(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, default=1)
    description = models.TextField()
    image =  models.ImageField(blank=True)
    
    def __str__(self):
        return self.title
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self):
        self.update_post()
    
    @classmethod
    def search_by_category(cls,search_term):
        posts = cls.objects.filter(category__name__icontains=search_term)
        return posts
class PostImage(models.Model):
    post = models.ForeignKey(Post, default = None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/',default = 'default.jpg')

    def __str__(self):
        return self.post.title






