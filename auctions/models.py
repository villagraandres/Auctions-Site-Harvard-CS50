from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
import pytz


    
class User(AbstractUser):
    pass

class Category(models.Model):
    name=models.CharField(max_length=100);
    
    def __str__(self):
        return f"{self.name}"
    



class List(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField();
    image= models.URLField();
    categories=models.ManyToManyField(Category,related_name="products")
    date =  models.DateTimeField( default=pytz.timezone('UTC').localize(datetime.datetime.now()));
    user=models.ForeignKey(User,related_name="userId",on_delete=models.CASCADE);
    closed=models.BooleanField();
    winner=models.ForeignKey(User,related_name="winner",on_delete=models.CASCADE,null=True);


    def __str__(self):
        return f"{self.title}"

class Watchlist(models.Model):
    products=models.ManyToManyField(List,related_name="lists");
    user=models.ForeignKey(User,related_name="owner",on_delete=models.CASCADE)

    def __str__(self):
        return f"Watchlist of {self.user}"

class Bid(models.Model):
    product=models.ForeignKey(List,on_delete=models.CASCADE,related_name="bidsProduct");
    user=models.ForeignKey(User,related_name="bids",on_delete=models.CASCADE);
    bid=models.IntegerField();

    def __str__(self):
        return f"Bid for {self.product} for {self.bid}"
    

class Comment(models.Model):
    product=models.ForeignKey(List,related_name="comments",on_delete=models.CASCADE);
    content=models.TextField();
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment");
    date =  models.DateTimeField( default=pytz.timezone('UTC').localize(datetime.datetime.now()));

    def __str__(self):
        return f"Comment in {self.product}: {self.date}";

