from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #this line defines our model (it is an object)
#class is a special keyword that indicates that we are defining an object.
#Post is the name of our model. Always start a class name with an uppercase letter.
#models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
    #models.ForeignKey – this is a link to another model.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #models.CharField – this is how you define text with a limited number of characters.
    title = models.CharField(max_length=200)
    #models.TextField – this is for long text without a limit. Sounds ideal for blog post content, right?
    text = models.TextField()
    #models.DateTimeField – this is a date and time.
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #we MUST indent our methods inside the class
    #defining publish method
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    #when we call __str__() we will get a text (string) with a Post title.
    def __str__(self):
        return self.title
