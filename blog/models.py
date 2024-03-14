from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    mobile_number = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name