from optparse import TitledHelpFormatter
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User=get_user_model()

class Author(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    thumb=models.ImageField(upload_to='pics')


    def __str__(self):
        return self.user.username 

class Posts(models.Model):
    image = models.ImageField(upload_to='images')
    Title= models.CharField(max_length=75)
    description = models.TextField()
    category = models.CharField(max_length= 50)
    Author= models.ForeignKey(Author,on_delete=models.CASCADE)
    Date= models.DateTimeField()

    def __str__(self):
        return self.Title

