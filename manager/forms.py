from django import forms

from product.models import Category, Product, Subcategory
from customer.models import Slider


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =["name","image"]

        widgets = {
            "name":forms.widgets.TextInput(attrs={"placeholder":"Category Name","class":"form-control"}),
            "image":forms.widgets.FileInput(attrs={"class":"form-control"}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =["name","sub_category","price","description","image"]


        widgets = {
            "name":forms.widgets.TextInput(attrs={"placeholder":"Product Name","class":"form-control"}),
            "sub_category":forms.widgets.Select(attrs={"class":"form-control"}),
            "price":forms.widgets.NumberInput(attrs={"placeholder":"Product Price","class":"form-control"}),
            "description":forms.widgets.Textarea(attrs={"placeholder":"Product Description","class":"form-control"}),
            "image":forms.widgets.FileInput(attrs={"class":"form-control"})
        }

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ["name","image","parent"]


        widgets ={
            "name":forms.widgets.TextInput(attrs={"placeholder":"Subcategory Name","class":"form-control"}),
            "image":forms.widgets.FileInput(attrs={"class":"form-control"}),
            "parent":forms.widgets.Select(attrs={"class":"form-control"})
        }


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ["name","image"]


        widgets ={
            "name":forms.widgets.TextInput(attrs={"placeholder":"Slider Name","class":"form-control"}),
            "image":forms.widgets.FileInput(attrs={"class":"form-control"}),
           
        }


class AddToCartForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    product_id = forms.IntegerField(widget=forms.HiddenInput())