from django.db import models

# Create your models here.
class Users(models.Model):
	rollno=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	aemail=models.CharField(max_length=30)
	bcat=models.CharField(max_length=30)
	aadhar=models.CharField(max_length=30)
	college=models.CharField(max_length=30)
	address=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	class Meta:
		db_table='Users'
class Blog(models.Model):
	blogid=models.CharField(max_length=30)
	userid=models.CharField(max_length=30)
	subject=models.CharField(max_length=30)
	blogtext=models.CharField(max_length=250)
	rating=models.IntegerField()
	class Meta:
		db_table='Blog'

	
		