from django.db import models
from django.contrib.auth.models import User



def upload_image(instance,filename):
    return "media/{user}/{filename}/".format(user=instance.user,filename=filename)

class Status(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    content = models.TextField(max_length=500,blank=True, null=True)
    image = models.ImageField(upload_to = upload_image ,blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)[:30]

    class Meta:
        verbose_name = "Status Post"
        verbose_name_plural = "Status Posts"    
