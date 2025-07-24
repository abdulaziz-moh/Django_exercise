from django.db import models

# Create your models here.

#------------------------------------------------------------------------------------------#
# for ONE TO MANY RELATIONSHIP (ForeignKey relaitonshiop)
#------------------------------------------------------------------------------------------#

class Departments(models.Model):
    name = models.CharField(max_length=255)
    
class Employees(models.Model):   # The foreign key is placed in the many side
    name = models.CharField(max_length=255)
    departments = models.ForeignKey(Departments,on_delete = models.CASCADE)
    
    # another example
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

#------------------------------------------------------------------------------------------#
# for ONE TO ONE RELTIONSHIP
#------------------------------------------------------------------------------------------#

class Product(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)  
    # in reality we don't need to set the primary key explictly, because django will handle it implicitly by creating a primary key named "id"
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class ProductDetail(models.Model):  # we put the OneToOneField on the dependent size for many reasons like: 
    # Reflect real-world ownership and dependency(a product detail is inforced to have a product first but not the reverse)
    # Avoid unnecessary NULLs (if we put the the onetoonefield in the product table it may have a null value because it's not necessary for product to have a productdetail)
    # Keep normalization and efficiency(for the upper benefits)
    # description = models.TextField()
    # category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.OneToOneField(Product,on_delete = models.CASCADE, related_name= "productdetail")
    
#------------------------------------------------------------------------------------------#
# for MANY TO MANY RELATIONSHIP (we can put the ManyToManyField anywhere we want)
#------------------------------------------------------------------------------------------#
 
class Student(models.Model):
    name = models.CharField(max_length=255)
    
class Cource(models.Model):
    c_name = models.CharField(max_length=255)
    students = models.ManyToManyField(Student,related_name="cources")   # the manytomany field can't have a on_deleted attribute