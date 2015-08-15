from django.db import models

class signup(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth=models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    country = models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    email_adress=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
    
    def __unicode__(self): 
        return self.first_name

class Login(models.Model):
    email_adress=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
    
    def __unicode__(self): 
        return self.email_adress

