from django.db import models

# Create your models here.


    
class Author(models.Model):
    AuthorID = models.CharField(max_length=20,primary_key = True)
    Name = models.CharField(max_length=50)
    Age = models.IntegerField(max_length=3)
    Country = models.CharField(max_length=50)
    
class Book(models.Model):
    ISBN = models.CharField(max_length=20,primary_key = True)
    Title = models.CharField(max_length=50)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=50)
    PublishDate = models.DateField()
    Price = models.IntegerField(max_length=10)