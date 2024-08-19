from django.db import models

# Create your models here.
class Pictures(models.Model):
    description = models.CharField(max_length= 500, blank=True, null=True)
    image = models.ImageField(upload_to='pictures/')
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.pic_name}'

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'