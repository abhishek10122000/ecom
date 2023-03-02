from django.shortcuts import render,redirect
from .models import *
from .form import CreateAccount
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login as loginFun, logout
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



# def insertuser(r):
#     form=UseruForm(r.POST or None, r.FILES or None)
#     if r.method=="POST":
#         if form.is_valid():
#             print(form)
#             form.save()
#             return redirect(home)
        

#     return render(r,'admin/createaccount.html',{'forms':form})
def createaccount(r):
    form=CreateAccount(r.POST or None ,r.FILES or None)
    if r.method== "POST":
        if form.is_valid():
            form.save()
            return redirect(login)
    data={}
    data['category']=getCatgory()
    data['forms']=form
    return render(r,'auth/createaccount.html',data)

def login(r):
    form=AuthenticationForm(r.POST or None)
    if r.method== "POST":
        username=r.POST.get('username')
        password=r.POST.get('password')
        user=authenticate(username=username, password=password)
        if user is not None:
            loginFun(r,user)
            return redirect(home)
    data={}
    data['category']=getCatgory()
    data['forms']=form
    return render(r,'auth/createaccount.html',data)
