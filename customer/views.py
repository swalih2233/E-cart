from django.shortcuts import render,reverse
from django.shortcuts import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from customer.models import Slider, Customer
from product.models import Product, Category
from users.models import User
from order.models import Orderitem,Order


@login_required(login_url='/login/')
def index(request):
    sliders=Slider.objects.all()
    products= Product.objects.all()
    categorys= Category.objects.all()
  
    

    context ={

              "title":"E-cart",
              "sliders":sliders,
              "products":products,
              "categorys":categorys
      }

  
    
    return render(request, "customerr/index.html", context=context)



@login_required(login_url='/login/')
def cart(request):
  user = request.user
  order_items = Orderitem.objects.filter(customer=user)
  
  

  

  context = {
           "title":"E-cart",
           "order_items":order_items
  }
  
  return render(request, 'customerr/cart.html',context=context)


@login_required(login_url='/login/')
def single(request,id):
      single= Product.objects.get(id=id)
     



      context={
        "title":"E-cart",
        "single":single,
      }

      return render(request, 'customerr/single.html',context=context)



def login(request):
   if request.method == 'POST':
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")


        if phone_number and password:
                user = authenticate(request, phone_number=phone_number, password=password)
                if user is not None:
                    auth_login(request, user)

                    return HttpResponseRedirect(reverse("customer:index"))
                
                else:
                    context ={
                        "title":"Login",
                        "error":True,
                        "message":"invalid credentials"
                    }

                return render(request, "customerr/login.html", context=context)
         
   else:
        context ={
            "title":"Login",
        }
        return render(request, "customerr/login.html", context=context)
   

def logout(request):
  
    auth_logout(request)

    return HttpResponseRedirect(reverse("customer:index"))




def register(request):
    if request.method == 'POST':
       phone_number = request.POST.get("phone_number")
       first_name = request.POST.get("first_name")
       last_name = request.POST.get("last_name")
       password = request.POST.get("password")

       user = User.objects.create_user(
          phone_number =phone_number,
           first_name = first_name,
           last_name = last_name,
           password = password,
           is_customer=True
       )

       user.save()

       customer= Customer.objects.create(
           user=user

          
       )

       customer.save()

       return HttpResponseRedirect(reverse("customer:login"))
    
    else:
       context={
           "title":"Create account",
       }
    
       return render(request, "customerr/register.html", context=context)
    


@login_required(login_url='/login/')   
def check(request):
  user=request.user
  order_items = Orderitem.objects.filter(customer=user)

 


  context = {
           "title":"E-cart",
           "order_items":order_items
  }
  
 
  return render(request, 'customerr/check.html', context=context)


def cart_add(request,id):
    user=request.user
    product = Product.objects.get(id=id)


    amount = product.price

    order_item = Orderitem.objects.create(
        customer = user,
        product = product,
        qty = 1,
        amount= amount,
    )
    order_item.save()
    
    return HttpResponseRedirect(reverse("customer:index"))


def cart_minus(request,id):
    order_item =Orderitem.objects.get(id=id)
    order_item.qty -= 1
    order_item.amount -= order_item.product.price
    order_item.save()

    if order_item.qty == 0:
        order_item.delete()

    return HttpResponseRedirect(reverse("customer:cart"))



def cart_plus(request,id):
    order_item =Orderitem.objects.get(id=id)
    order_item.qty += 1
    order_item.amount += order_item.product.price
    order_item.save()

    return HttpResponseRedirect(reverse("customer:cart"))
    

