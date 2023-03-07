from django.db import models


# Create your models here.

class SignUp(models.Model):
	fname=models.CharField(max_length=50)
	lname=models.CharField(max_length=50)
	contact=models.CharField(max_length=50)
	address=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	user=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	pic=models.ImageField(upload_to='img/')

class Categary(models.Model):

	cat=models.CharField(max_length=60)
	dt=models.DateField()

class Policy(models.Model):
	cat=models.CharField(max_length=60)
	name=models.CharField(max_length=60)
	sumassu=models.CharField(max_length=60)
	premium=models.CharField(max_length=60)
	tenure=models.CharField(max_length=60)

class PolicyRecord(models.Model):
    customer= models.CharField(max_length=100)
    policy= models.CharField(max_length=100)
    status = models.CharField(max_length=100,default='Pending')
    creation_date =models.DateField(auto_now=True)

class Question1(models.Model):
	customer=models.CharField(max_length=50)
	description=models.CharField(max_length=500)
	admin_comment=models.CharField(max_length=200,default='Nothing')
	creation_date =models.DateField(auto_now=True)
    