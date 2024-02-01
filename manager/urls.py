from django.urls import path

from manager import views

app_name ="manager"

urlpatterns=[
    path("",views.dashboard, name="dashboard"),
    path("categories/",views.categories, name="categories"),
    path("sub_categories/",views.sub_categories, name="sub_categories"),
    path("order/",views.order, name="order"),
    path("customer/",views.customer, name="customer"),
    path("product/",views.product, name="product"),
    

     
    path("categories/add/", views.category_add, name="category_add"),
    path("categories/delete/<int:id>/",views.category_del, name="category_del"),
    path("categories/edit/<int:id>/", views.category_edit, name="category_edit"),

    path("sub_categories/add/", views.sub_categories_add, name="sub_categories_add"),
    path("sub_categories/delete/<int:id>/", views.sub_categories_del, name="sub_categories_del"),
    path("sub_categories/edit/<int:id>/", views.sub_categories_edit, name="sub_categories_edit"),


    path("product/add/", views.product_add, name="product_add"),
    path("product/delete/<int:id>/",views.product_del, name="product_del"),
    path("product/edit/<int:id>/", views.product_edit, name="product_edit"),



    path("",views.index, name="index"),
    path("cart/",views.cart, name="cart"),
       
    path("slider/add/", views.slider_add, name="slider_add"),
    path("slider/delete/<int:id>/",views.slider_del, name="slider_del"),
    path("slider/edit/<int:id>/", views.slider_edit, name="slider_edit"),

    path("slider/",views.slider, name="slider"),

    path("login/",views.login, name="login"),
    path("logout/",views.logout, name="logout"),


    
    
    
]




