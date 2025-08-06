from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Cource,Student,ProductDetail

# Create your views here.

def display_homepage(request):
    return render(request, "homepage.html")
def product_List(request):
    products = Product.objects.all()
    return render(request, "display_products.html",{"products":products})
def product_detail(request,name_of_product = "product_detail"):
        
    product = get_object_or_404(Product, name = "Ergonomic Office Chair")
    return render(request, "product_detail.html", {"product":product})

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
    # product = Product.objects.get(id = 1)
    # ProductDetail.objects.create(
    #     product =product,
    # )
    # product = Product.objects.get(id = 2)
    # ProductDetail.objects.create(
    #     product =product,
    # )
    # product = Product.objects.get(id = 3)
    # ProductDetail.objects.create(
    #     product =product,
    # )
    # product = Product.objects.get(id = 4)
    # ProductDetail.objects.create(
    #     product =product,
    # )
    # product = Product.objects.get(id = 5)
    # ProductDetail.objects.create(
    #     product =product,
    # )
    
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
           
    pairs = zip(products,details)  # we do this because we can not iterate over list using and index(like by using)
        
    return render(request,"all_product_with_detail.html",{"pairs":pairs})


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
    # 
    
def create_student(request):
        # student 1
    Student.objects.create(
        name='Abebe Chala',
    )
    cources = Cource.objects.all()
    students = Student.objects.all()
    return render(request, "display_stu_crc.html",{"students":students,"cources":cources})

def create_cource(request):
        # cource 1
    Cource.objects.create(
        c_name='Fundamental of programming 1',
    )
    cources = Cource.objects.all()
    students = Student.objects.all()
    return render(request, "display_stu_crc.html",{"students":students,"cources":cources})
def enrlol_student(request):
    stu = "Abebe Chala"
    crc = "Fundamental of programming 1"
    student1 = Student.objects.get(name = stu)
    cource1 = Cource.objects.get(c_name = crc)
    
    student1.cources.add(cource1)
    
    students = Student.objects.all()
    cources = Cource.objects.all()
    
    return render(request,"display_stu_crc.html",{"students":students, "cources":cources})

# def display_stu_crc(request):
#     # because it's many to many we use prefetch_related
    
#     # without prefetch_related   
#     stu_s = Student.objects.all() # no prefetch_related here
#     for stu in stu_s:
#         print(f"student name: {stu.name}")
#         for cource in stu.cources.all():
#             print(cource.c_name, end="  ")
            
#     # with prefetch_related(arg)
#     pairs = Student.objects.prefetch_related('cources')

#     return render(request,"stu_vs_cource.html",{"pairs":pairs})
     
from django.views.generic import ListView,DetailView
class display_stu_crc(ListView):
    template_name  = "stu_vs_cource.html"
    queryset = Student.objects.prefetch_related('cources')  # if you specifically want prefetch related

    # model = Student  # if you let django do it any way, possibly not prefetch related
    context_object_name = "pairs"




class product_detail(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"

def tobasehtml(request):
    return render(request, "base.html")


from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # render(request,"base.html")
            return redirect('/Product/basehtml/') # USED absolute path "which is the path start from '/' and it will be appended to the http://127.0.0.1:8000/"
                                                  # but if we use the relative path "whic don't have '/' at the start , this path will be appended to the path the browser have in its url bar" 
                                                  # but from this ambiguty it's recomended practice to use name instead of the pattern so that django can handle it 
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form':form})
            

from . forms import ContactForm
def contact_veiw(request):
    if request.method == 'post': 
        form = ContactForm(request.POST)
    
        if form.is_valid():
            name = form.cleaned_data('name')
            email = form.cleaned_data('email')
            message = form.cleaned_data('message')
            
            return render(request,'contact.html',{'form': ContactForm() ,'succes': True })
    
    else:
        return render(request,'contact.html', {'form':ContactForm()})
    