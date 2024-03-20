from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]
    
    def pub_date(self):
        return self.public_date.strftime("%b %e, %y")
    
    def __str__(self):
        return self.title
    