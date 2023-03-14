from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .form import *
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


def AddToCart(r,slug):
    product=get_object_or_404(Product,slug=slug)
    order_item,created=OrderItem.objects.get_or_create(user=r.user, ordered=False, item=product)
    order_qs=Order.objects.filter(user=r.user, ordered=False)

    if order_qs.exists():
        order=order_qs[0]

        if(order.items.filter(item__slug=slug).exists()):
            order_item.qty +=1
            order_item.save()

        else:
            order.items.add(order_item)

        return redirect(myCart)
    else:
        order=Order.objects.create(user=r.user)
        order.items.add(order_item)
        return redirect(home)
    
    
def removeCart(r,slug):
    product=get_object_or_404(Product,slug=slug)
    order=Order.objects.get(user=r.user, ordered=False)
    order_item=OrderItem.objects.get(user=r.user, ordered=False, item=product)

    if order:

        if(order.items.filter(item__slug=slug).exists()):
            if  order_item.qty <=1:
                order_item.delete()

            else:
                order_item.qty -=1
                order_item.save()

        return redirect(myCart)
    
    

def myCart(r):
    data={}
    # data['order']=Order.objects.get(user=r.user,ordered=False)
    data['order']=Order.objects.get(user=r.user, ordered=False)
    print(data)
    return render(r,'cart.html',data)



def checkCode(code):
    try:
        coupon = Coupon.objects.get(cod=code)
        return True
    except:
        return False
    
def getCoupon(code):
    try:
        coupon = Coupon.objects.get(cod=code)
        return coupon 
    except:
        # invalid coupon
        return redirect(myCart)

def addCoupon(r):
    code = r.POST.get('code')

    if checkCode(code):
        coupon = getCoupon(code)
        order = Order.objects.get(user=r.user, ordered=False)
        order.coupon = coupon
        order.save()
        # successfully coupon applied
    return redirect(myCart)

def removeCoupon(r):
    order = Order.objects.get(user=r.user, ordered=False)
    order.coupon = None
    order.save()
    return redirect(myCart)


def checkout(r):
    add=Address.objects.filter(user=r.user)
    form=AddressForm(r.POST or None)
    if r.method =="POST":
        if form.is_valid():
            f=form.save(commit=False)
            f.user=r.user
            f.save()
            return redirect(checkout)
        

    return render(r, 'checkout.html',{'forms':form,'add':add})
