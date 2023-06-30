from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Batch(models.Model):
    batch_name = models.CharField(max_length=50)
    batch_time = models.TimeField()

    def __str__(self):
        return self.batch_name


class Login(AbstractUser):
    is_trainer = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    name = models.CharField(max_length=25, null=True)
    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    contact_no = models.IntegerField(null=True)
    photo = models.ImageField(upload_to='profile', null=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True, blank=True)
    batch_time = models.CharField(max_length=200, null=True, blank=True)


class Equipments(models.Model):
    name = models.CharField(max_length=25, null=True)
    type = models.CharField(max_length=25, null=True)
    photo = models.ImageField(upload_to='profile', null=True)

    def __str__(self):
        return self.name


class Bill(models.Model):
    name = models.ForeignKey(Login, on_delete=models.CASCADE)
    bill_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    paid_on = models.DateField(auto_now=True)
    status = models.IntegerField(default=0)


class Attendance(models.Model):
    name = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='attendance')
    attendance = models.CharField(max_length=10)
    date = models.DateField()


class Payment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    payment = models.CharField(max_length=250)
    card_number = models.IntegerField()
    card_cvv = models.IntegerField()
    card_expiry_month = models.CharField(max_length=250)
    card_expiry_year = models.CharField(max_length=250)

