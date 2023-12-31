from django.db import models

# Create your models here.


class Email(models.Model):

    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sendtime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
       return self.email
    
