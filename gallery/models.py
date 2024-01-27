# models.py
from django.db import models
from django_resized import ResizedImageField
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='basic/art_gallery/') 
    description = models.TextField()
    # upload_date = models.DateTimeField(auto_now_add=True, default=timezone.now)  # Manually define a default value
    
    # ImageFields
    squareImage = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_square.jpg', upload_to='art_gallery/square')
    landImage = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], default='default_land.jpg', upload_to='art_gallery/landscape')
    tallImage = ResizedImageField(size=[1618, 2878], crop=['middle', 'center'], default='default_tall.jpg', upload_to='art_gallery/tall')

    # Related Fields
    categories = models.ManyToManyField(Category, related_name='images')

    def __str__(self):
        return self.title
    


class Review(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    created_at = models.DateTimeField( default=timezone.now)  
    # auto_now_add=True,
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    anonymous= models.BooleanField( default=False, null=True)
    rate=models.IntegerField( default=5)


    def __str__(self):
        username = self.user.username if self.user else "Anonymous"
        return f"{username}'s review on {self.image.title}: {self.rate}"

    def save(self, *args, **kwargs):
        # Set the user field to the currently logged-in user
        if not self.user_id:
            self.user = kwargs.pop('user', None)

        super().save(*args, **kwargs)