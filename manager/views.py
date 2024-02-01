from django.shortcuts import render,reverse
from django.shortcuts import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


from product.models import Category, Subcategory, Product
from order.models import Order
from customer.models import Customer, Slider

from manager.forms import CategoryForm, SubcategoryForm, ProductForm, AddToCartForm
from manager.forms import SliderForm



@login_required(login_url='/manager/login/')
def dashboard(request):
    orders = Order.objects.all().count()
    products = Product.objects.all().count()
    customers = Customer.objects.all().count()
    
    context ={

             "title":"Ecommerce",
             "orders": orders,
             "products":products,
             "customers":customers
    }
      
    
    
    return render(request, "manager/dashboard.html", context=context)


def categories(request):
    categorys = Category.objects.all()
 
    context ={
        "title":"Ecommerce",
        "categorys": categorys,
    }
    return render(request, "manager/categories.html", context=context)


def sub_categories(request):
    subcategorys = Subcategory.objects.all()

    context ={
        "title":"Ecommerce",
        "subcategorys":subcategorys
    }

    return render(request, "manager/sub_categories.html", context=context)


def order(request):
    orders = Order.objects.all()
    
    context ={
        "title":"Ecommerce",
        "orders":orders,


    }
    return render(request, "manager/order.html", context=context)



def product(request):
    products = Product.objects.all()

    context ={
        "title":"Ecommerce",
        "products":products


    }


    return render(request, "manager/product.html", context=context)


def customer(request):
    customers = Customer.objects.all()
  
    context ={
        "title":"Ecommerce",
        "customers":customers,
        "slider":slider


    }

    return render(request, "manager/customer.html", context=context)



def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            subcategory = instance.sub_category
            category = subcategory.parent
            instance.category = category
            instance.save()

            return HttpResponseRedirect(reverse("manager:product"))
        else:
            pass

    else:
        form = ProductForm()
        context={
            "title":"manager | dashboard",
            "form":form
        }

        return render(request, "manager/add_product.html", context=context)
    


def product_del(request, id):
    
    products = Product.objects.get(id=id)
    products.delete()

def product_edit(request, id):
    instance = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse, ("manager:product"))
        
        else:
            pass

    else:
        form = ProductForm(instance=instance)
        context={
            "title":"manager | dashboard",
            "form":form
        }

        return render(request, "manager/add_product.html", context=context)




def category_add(request):
    if request.method == 'POST':
        form =  CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse("manager:categories"))
        
        else:
            pass


    else:
        form = CategoryForm()
        context={
            "title":"manager | dashboard",
            "form":form
        }

        return render(request, "manager/add_category.html", context=context)


def category_del(request, id):
    
    categorys = Category.objects.get(id=id)
    categorys.delete()

    return HttpResponseRedirect(reverse("manager:categories"))


def category_edit(request,id):
    instance = Category.objects.get(id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse("manager:categories"))
        
        else:
            form = CategoryForm(instance=instance)
            context={
                "title":"manager | dashboard",
                "form":form
            }

            return render(request, "manager/add_category.html", context=context)

    else:
        form = CategoryForm(instance=instance)
        context={
            "title":"manager | dashboard",
            "form":form
        }

        return render(request, "manager/add_category.html", context=context)

def sub_categories_add(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST,request.FILES,)
        if form.is_valid():
            instance =form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse("manager:sub_categories"))
        
        else:
            pass


    else:
        form = SubcategoryForm()
        context =  {
            "title": "manager | dashboard",
            "form":form
        }
        return render(request,"manager/add_subcategory.html", context=context)


def sub_categories_del(request, id):
    sub_categories =Subcategory.objects.get(id=id)
    sub_categories.delete()

    return HttpResponseRedirect(reverse("manager:sub_categories"))

def sub_categories_edit(request, id):
    instance = Subcategory.objects.get(id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse("manager:sub_categories"))
        
        else:
            pass

    else:
        form = SubcategoryForm(instance=instance)
        context={
            "title":"manager | dashboard",
            "form":form
        }

        return render(request, "manager/add_subcategory.html", context=context)
    


def index(request):
    sliders = Slider.objects.all()

    context = {
         "title":"E-cart",
         "sliders":sliders
    }
       
    
    return render(request, "customerr/index.html", context=context)



def cart(request):
    return render(request, "manager/cart.html")
  
def slider_add(request):
    if request.method == 'POST':
        form = SliderForm(request.POST,request.FILES,)
        if form.is_valid():
            instance =form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse("manager:slider"))
        
        else:
            pass


    else:
        form = SliderForm()
        context =  {
            "title": "customer | index",
            "form":form
        }
        return render(request,"manager/add_slider.html", context=context)


def slider_del(request, id):
    sliders =Slider.objects.get(id=id)
    sliders.delete()

    return HttpResponseRedirect(reverse("manager:slider"))

def slider_edit(request,id):
    instance = Slider.objects.get(id=id)
    if request.method == "POST":
        form = SliderForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse("manager:slider"))
        
        else:
            pass

    else:
        form = SliderForm(instance=instance)
        context={
            "title":"customer | index",
            "form":form
        }

        return render(request, "manager/add_slider.html", context=context)


def slider(request):
    sliders = Slider.objects.all()

    context = {
         "title":"Ecommerce",
         "sliders":sliders
    }
       
    
    return render(request, "manager/slider.html", context=context)


def login(request):
    if request.method == 'POST':
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")


        if phone_number and password:
                user = authenticate(request, phone_number=phone_number, password=password)
                if user is not None:
                    auth_login(request, user)

                    return HttpResponseRedirect(reverse("manager:dashboard"))
                
                else:
                    context ={
                        "title":"Login",
                        "error":True,
                        "message":"invalid credentials"
                    }

                return render(request, "manager/login.html", context=context)
         
    else:
        context ={
            "title":"Login",
        }
        return render(request, "manager/login.html", context=context)
    
        


def logout(request):
  
    auth_logout(request)

    return HttpResponseRedirect(reverse("manager:dashboard"))

