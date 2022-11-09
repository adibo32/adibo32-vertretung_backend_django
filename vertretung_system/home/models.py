from django.db import models
import uuid


class UserType(models.Model):
    id = uuid
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class User(models.Model):
    
    id = uuid
    email = models.EmailField(max_length=100, default='')
    password = models.CharField(max_length=50)
    lehrer_init = models.CharField(max_length=100)
    user_type_id = models.ForeignKey(UserType, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.lehrer_init
    

class Antrag(models.Model):
    id = uuid
    creator_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    to_user_id = models.CharField(max_length=100)
    datum = models.DateTimeField()
    def __str__(self):
        return self.to_user_id