from django.shortcuts import render,get_object_or_404
from .models import Product

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
    #     # Product 1
    # Product.objects.create(
    #     id=1,
    #     name='Wireless Bluetooth Headphones',
    #     description='High-fidelity sound with noise-cancelling features and 20-hour battery life.',
    #     price=79.99,
    #     category='Electronics'
    # )

    # # Product 2
    # Product.objects.create(
    #     id=2,
    #     name='Organic Green Tea - 100 bags',
    #     description='Sustainably sourced organic green tea, rich in antioxidants. Perfect for a calming brew.',
    #     price=12.50,
    #     category='Food & Beverages'
    # )

    # Product 3
    Product.objects.create(
        # id=3,
        name='Ergonomic Office Chair',
        description='Adjustable lumbar support, breathable mesh, and smooth-rolling casters for ultimate comfort.',
        price=249.00,
        category='Home & Office'
    )
    products = Product.objects.all()
    return render(request,"display_products.html",{"products":products})

    # # Product 4
    # Product.objects.create(
    #     id=4,
    #     name='Stainless Steel Water Bottle - 1 Liter',
    #     description='Double-walled insulation keeps drinks cold for 24 hours and hot for 12 hours.',
    #     price=19.95,
    #     category='Kitchen & Dining'
    # )

    # # Product 5
    # Product.objects.create(
    #     id=5,
    #     name='Fiction Novel: "The Midnight Library"',
    #     description='A captivating story about choices, regrets, and finding a different life.',
    #     price=15.75,
    #     category='Books'
    # )
    
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
        