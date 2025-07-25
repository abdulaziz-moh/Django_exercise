from django.shortcuts import render,get_object_or_404
from .models import Product,Cource,Student,ProductDetail

# Create your views here.

def display_homepage(request):
    return render(request, "homepage.html")
def product_List(request):
    products = Product.objects.all()
    return render(request, "display_products.html",{"products":products})
def product_detail(request,name_of_product = "product_detail"):
        
    product = get_object_or_404(Product, name = "Ergonomic Office Chair")
    return render(request, "product_detail.html", {"product":product,"name_of_product":name_of_product})

def create_product(request):
        # Product 1
    Product.objects.create(
        id=1,
        name='Wireless Bluetooth Headphones',
        description='High-fidelity sound with noise-cancelling features and 20-hour battery life.',
        price=79.99,
        category='Electronics',
    )

    # Product 2
    Product.objects.create(
        id=2,
        name='Organic Green Tea - 100 bags',
        description='Sustainably sourced organic green tea, rich in antioxidants. Perfect for a calming brew.',
        price=12.50,
        category='Food & Beverages',
    )

    # Product 3
    Product.objects.create(
        id=3,
        name='Ergonomic Office Chair',
        description='Adjustable lumbar support, breathable mesh, and smooth-rolling casters for ultimate comfort.',
        price=249.00,
        category='Home & Office',
    )
    # return render(request,"display_products.html",{"products":products})

    # Product 4
    Product.objects.create(
        id=4,
        name='Stainless Steel Water Bottle - 1 Liter',
        description='Double-walled insulation keeps drinks cold for 24 hours and hot for 12 hours.',
        price=19.95,
        category='Kitchen & Dining',
    )

    # Product 5
    Product.objects.create(
        id=5,
        name='Fiction Novel: "The Midnight Library"',
        description='A captivating story about choices, regrets, and finding a different life.',
        price=15.75,
        category='Books',
    )
    products = Product.objects.all()
    return render(request,"display_products.html",{"products":products})


def add_product_discription(request):   # dependent on the product 
    product = Product.objects.get(id = 1)
    ProductDetail.objects.create(
        product =product,
    )
    product = Product.objects.get(id = 2)
    ProductDetail.objects.create(
        product =product,
    )
    product = Product.objects.get(id = 3)
    ProductDetail.objects.create(
        product =product,
    )
    product = Product.objects.get(id = 4)
    ProductDetail.objects.create(
        product =product,
    )
    product = Product.objects.get(id = 5)
    ProductDetail.objects.create(
        product =product,
    )
    
    # with out select_related
    products = Product.objects.all()
    for prod in products:
        detail = prod.productdetail  # each will have a single sql request 
        print(detail)
    
    # with select_related
    products =Product.objects.select_related("productdetail")
    details = []
    for pord in products:
        detail = prod.productdetail  # all are requested once first at     products =Product.objects.select_related("productdetail")
        details.append(detail)
            
        
    return render(request,"all_product_with_detail.html",{"products":products,"details":details})


def update_product(request, product_name = "Ergonomic Office Chair",changed_attribute = "price" , changed_value = "300"):
    try:
        product = Product.objects.get(name = product_name)


        if changed_attribute == "name":
            product.name = changed_value
        elif changed_attribute == "description":
            product.description = changed_value
        elif changed_attribute == "price":
            product.price = changed_value
        elif changed_attribute == "category":
            product.category = changed_value
        product.save()
        return render(request, "update.html", {"message":f"{product_name} updated succesfully!!", "product":product})
    except Product.DoesNotExist:
        return render(request, "update.html", {"message":f"{product_name} doesn't exist in the dataset!"})

def delete_product(request, product_name = "Ergonomic Office Chair"):
    try:
        product = Product.objects.get(name = product_name)
        product.delete()
        return render(request, "update.html", {"message":f"{product_name} deleted succesfully"})
    except Product.DoesNotExist:
        return render(request, "update.html",{"message":f"{product_name} doesn't exist in the database, please check the name again!"})

# -------------prefetch_related---------------
# Works(used) for many-to-many and reverse foreign key relationships.
# Performs separate SQL queries, then joins in Python.


def functionwith_prefetch_related(request,product_name):
    try:
        product = Product.objects.get(name = product_name)
        
        
        return render(request, "",{"":""})
    except Product.DoesNotExist:
        return render(request, "",{"":""})
    
    
def create_student(request):
        # student 1
    Student.objects.create(
        name='Abebe Chala',
    )

def create_cource(request):
        # cource 1
    Cource.objects.create(
        c_name='Fundamental of programming 1',
    )
def enrlol_student(request):
    stu = "Abebe Chala"
    crc = "Fundamental of programming 1"
    student1 = Student.objects.get_or_create(name = stu)
    cource1 = Cource.objects.get_or_create(c_name = crc)
    
    student1.cources.add(cource1)
    
    students = Student.objects.all()
    cources = Cource.objects.all()
    
    return render(request,"display_stu_crc.html",{"students":students, "cources":cources})

def display_stu_crc(request):
    # because it's many to many we use prefetch_related
    
    # without prefetch_related   
    stu_s = Student.objects.all() # no prefetch_related here
    for stu in stu_s:
        print(f"student name: {stu.name}")
        for cource in stu.cources.all():
            print(cource.c_name, end="  ")
            
    # with prefetch_related(arg)
    stu_s = Student.objects.prefetch_related('cources')
    cource_for_each_stu = {}
    for stu in stu_s:
        print(f"student name: {stu.name}")
        crc = []
        for cource in stu.cources.all():
            crc.append(cource)
            print(cource.c_name, end="  ")
        cource_for_each_stu[stu] = crc
        
    return render(request,"display_stu_crc.html",{"students":stu_s, "cources":cource_for_each_stu})
     
