from django.db import models

# Create your models here.

STATUS = (('active', 'active'),('blank=True', 'inactive'))
LABELS = (('hot','hot'),('new','new'),('sale','sale'),('','default'))

class Category(models.Model):
    name = models.CharField(max_length= 300)
    slug = models.CharField(max_length= 300, unique=True)
    description = models.CharField(max_length= 300, blank=True)


    def __str__(self):
        return self.name




class SubCategory(models.Model):
    name = models.CharField(max_length= 300)
    slug = models.CharField(max_length= 300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length= 300,blank=True)


    def __str__(self):
        return self.name


class slider(models.Model):
    name = models.CharField(max_length= 300)
    slug = models.CharField(max_length= 300) #we use slug tyo information bhaira na jaos bhanera to protect your website.
    description = models.TextField(max_length= 300,blank = True)
    image = models.ImageField(upload_to = 'media' )
    rank = models.IntegerField()
    status = models.CharField(max_length= 300, choices = STATUS)

    def __str__(self):
        return self.name


class Product(models.Model):
        title = models.CharField(max_length=300)
        price = models.IntegerField()
        discounted_price = models.IntegerField(default=0)
        image = models.ImageField(upload_to='media')
        description =models.IntegerField()
        status = models.CharField(max_length=50,choices =STATUS)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
        labels = models.CharField(choices = LABELS, max_length=100,blank=True)

        def __str__(self):
            return self.title
            

class Ad(models.Model):
        name = models.CharField(max_length= 300)
        slug = models.CharField(max_length= 300) #we use slug tyo information bhaira na jaos bhanera to protect your website.
        description = models.TextField(max_length= 300)
        image = models.ImageField(upload_to = 'media' )
        rank = models.IntegerField()
        status = models.CharField(max_length= 300, choices = STATUS)
        
        def __str__(self):
            return self.name
