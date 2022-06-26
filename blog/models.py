from django.conf import settings
from django.db import models
from django.utils import timezone

#defines our model - it is an object
#class - keyword to indicate defining of an object
#Post - name of our model ***always start with a capital letter***
#models.Model - the Post is a Django Model, so Django knows it should be saved in a database
class Post(models.Model):
    #link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #how you define text with a limited number of characters
    title = models.CharField(max_length=200)
    #for long text without a limit 
    text=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #methods must be indented inside our class
    #publish method
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    #method that returns a text string with a Post title
    def __str__(self):
        return self.title

