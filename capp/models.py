from django.db import models

# Create your models here.
class register_tb(models.Model):
	fname=models.CharField(max_length=255)
	lname=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	phone=models.CharField(max_length=255)
	status=models.CharField(max_length=255)
	epassword=models.CharField(max_length=255)

class user_tb(models.Model):
	fname=models.CharField(max_length=255)
	lname=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	phone=models.CharField(max_length=255)
	epassword=models.CharField(max_length=255)

class turf_tb(models.Model):
	name=models.CharField(max_length=255)
	image=models.FileField(upload_to="turf",default="")
	owner=models.ForeignKey(register_tb, on_delete=models.CASCADE)
	address=models.CharField(max_length=255)
	status=models.CharField(max_length=255)
	# ratings=models.CharField(max_length=255)
	timing=models.CharField(max_length=255)
	price=models.CharField(max_length=255)

class cart_tb(models.Model):
	name=models.ForeignKey(user_tb, on_delete=models.CASCADE)
	owner=models.ForeignKey(register_tb,on_delete=models.CASCADE)
	price=models.CharField(max_length=255)
	turfid=models.ForeignKey(turf_tb, on_delete=models.CASCADE)
	totalprice=models.CharField(max_length=255)
	status=models.CharField(max_length=255)
	time=models.DateTimeField(max_length=255)
	btiming=models.CharField(max_length=255)
	date=models.CharField(max_length=255)


class signin_tb(models.Model):
	uname=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	
# class contact_tb(models.Model):
# 	name=models.CharField(max_length=255)
# 	email=models.CharField(max_length=255)
# 	message=models.CharField(max_length=255)

class payment_tb(models.Model):
	nameoncard=models.CharField(max_length=255)
	grandtotal=models.CharField(max_length=255)
	status=models.CharField(max_length=255)
	date=models.CharField(max_length=255)
	username=models.ForeignKey(user_tb, on_delete=models.CASCADE)
	cartid=models.ForeignKey(cart_tb, on_delete=models.CASCADE)

class feedback_tb(models.Model):
	uid=models.ForeignKey(user_tb, on_delete=models.CASCADE)
	turfid=models.ForeignKey(turf_tb, on_delete=models.CASCADE)
	owner=models.ForeignKey(register_tb,on_delete=models.CASCADE)
	feedback=models.CharField(max_length=255)
