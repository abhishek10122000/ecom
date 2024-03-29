"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home ,name='home'),

    path('category/<int:id>/',category,name='category'),
    path('productView/<slug>/',productView,name='productView'),
    path('search/',search,name='search'),
    path('createaccount/',createaccount, name="createaccount"),
    path('login/',login, name="login"),
    path('add-to-cart/<slug>/',AddToCart, name="addCart"),
    path('remove-from-cart/<slug>/',removeCart, name="removeCart"),

    path('cart/',myCart,name="cart"),
    path('addcoupon/',addCoupon,name="addcoupon"),
    path('removecoupon/',removeCoupon,name="removecoupon"),
    path('checkout/',checkout,name="checkout"),
    path('check-with-Save/',checkWithSave,name="checkwithsave"),
]
urlpatterns +=static(settings.MEDIA_URL,
                     document_root=settings.MEDIA_ROOT)