from django.urls import path

from customer import views

app_name ="customer"

urlpatterns=[
    path("",views.index, name="index"),
    path("cart/",views.cart, name="cart"),
    path("single/<int:id>/",views.single, name="single"),
    path("check/",views.check, name="check"),

    path("cart/add/<int:id>/",views.cart_add, name="cart_add"),
    path("cart/minus/<int:id>/",views.cart_minus, name="cart_minus"),
    path("cart/plus/<int:id>/",views.cart_plus, name="cart_plus"),


    path("register/",views.register, name="register"),
    path("login/",views.login, name="login"),
    path("logout/",views.logout, name="logout"),






    ]



