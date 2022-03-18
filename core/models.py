from crypt import methods
from pickle import FALSE
from django.db import models


# Create your models here.
class BookItem(models.Model):
    barcode = models.CharField(max_length=50)
    isreferenceOnly = models.BooleanField(default=FALSE)
    borrowed = models.DateField()
    dueDate = models.DateField()
    price = models.FloatField()
    format = models.CharField(max_length=50)

class Address(models.Model):
    streetAdress = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zicode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.streetAdress

class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    adress = models.ForeignKey(
        Address,
        on_delete=models.CASCADE
    )

class AcountStatus (models.Model):
    activate = models.BooleanField(default=False)
    closed = models.BooleanField(default=True)
    canceled = models.BooleanField(default=False)
    balcklisted = models.BooleanField(default=False)

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=50)
    status = models.ForeignKey(
        AcountStatus,
        on_delete=models.CASCADE
    )

    #def resetPassword(self):
        #return self.password = ''

class Library(models.Model):
    name = models.CharField(max_length=50)
    addres = models.ForeignKey(
        Address,
        on_delete=models.CASCADE
    )

    def getAdress(self):
        return self.addres

class Book(models.Manager):
    #ISBN = models.
    title = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    numberOfPages = models.IntegerField()

    def getTitle(self):
        return self.title

class Librarian(models.Manager):
    pass





