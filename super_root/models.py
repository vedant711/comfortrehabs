from django.db import models

# Create your models here.

class Joints(models.Model):
    id = models.IntegerField(primary_key=True)
    joint = models.CharField(max_length=100)

    def __str__(self):
        return self.joint
    
class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    arabic_description = models.TextField()
    swahili_description = models.TextField()
    chinese_description =  models.TextField()
    img_path = models.CharField(max_length=200)
    joint = models.ForeignKey(Joints, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email
    

class People(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    description = models.TextField()
    img_path = models.CharField(max_length=200)

    def __str__(self):
        return self.name