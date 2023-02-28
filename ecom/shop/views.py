from django.shortcuts import render
from .models import *
# Create your views here.
def getCatgory():
    return Category.objects.all()

def home(r):
    data={}
    data['category']=getCatgory()
    return render(r,'home.html',data)

def getProduct():
    return Product.objects.all()


def category(r,id):
    data={}
    data['category']=getCatgory()
    data['product']=Product.objects.filter(category=id)

    return render(r,'category.html',data)


def productView(r,slug):
    data={}
    data['category']=getCatgory()
    data['product']=Product.objects.get(slug=slug)

        
    return render(r,'productView.html',data)

def search(r):
    data={}
    data['category']=getCatgory()
    data['product']=Product.objects.filter(name__icontains=r.GET.get('search'))
    return render(r,'category.html',data)