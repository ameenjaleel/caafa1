from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,get_user_model,login,logout
from .forms import UserRestoLoginForm,UserRestoRegisterForm,RestoDashForm


def resto_login(request):
    form=UserRestoLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        return render(request,"resto_index.html")

    return render(request,"resto_login.html",{ "form":form })

def resto_register(request):
    form = UserRestoRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username,password=password)
        login(request,new_user)
        return render(request,"resto_index.html")
    return render(request,"resto_register.html",{"form":form})


def resto_logout(request):
    logout(request)
    return render(request,'index.html')

def resto_index(request):
    return render(request,'resto_index.html')

def resto_dash(request):
    form = RestoDashForm(request.POST or None)
    if form.is_valid():
        resto = form.save(commit=False)
        resto.resto_name = form.cleaned_data.get("resto_name")
        resto.product_name = form.cleaned_data.get("product_name")
        resto.product_cuisines = form.cleaned_data.get("product_cuisines")
        resto.product_img = form.cleaned_data.get("product_img")
        resto.product_about = form.cleaned_data.get("product_about")
        resto.product_price = form.cleaned_data.get("product_price")
        resto.save()
        return render(request,'resto_index.html')
    return render(request, 'resto_dash.html',{ "form":form })
