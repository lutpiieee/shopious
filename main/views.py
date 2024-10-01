from django.shortcuts import render, redirect, reverse, get_object_or_404   # Tambahkan import redirect di baris ini
from main.forms import addItemForm
from main.models import AddItem
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url='/register')
def show_main(request):
    addItem_entries = AddItem.objects.all()  # Retrieve all AddItem entries

    context = {
        'nama': 'Adidas Samba Nylon Wales Bonner Core Black',
        'harga': 'IDR 7,770,000',
        'deskripsi': 'A few months after the recognizable version, Wales Bonner and adidas reveal a new pack around the legendary Samba model. This Adidas Samba Nylon Wales Bonner Core Black presents a base in black nylon horse dressing, accompanied by a black leather mudguard. The three adidas stripes provide contrast with their white leather design, extending to the heel tab and tongue, marked by the London designer’s touch. A gum sole adds the final touch, preserving the heritage of this iconic soccer shoe.',
        'addItem_entries': addItem_entries,  # Add this to the context
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def show_xml(request):
    data = AddItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = AddItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = AddItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")    

def show_json_by_id(request, id):
    data = AddItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def create_add_item(request):
    form = addItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_item_form.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(AddItem, id=product_id)
    reviews = ReviewItem.objects.filter(product=product)  # Assuming you have a product foreign key in ReviewItem

    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'product_detail.html', context)

def edit_product(request, id):
    # Get the product by its id
    product = get_object_or_404(AddItem, pk=id)

    # Create a form instance, pre-filled with the current product data
    form = addItemForm(request.POST or None, instance=product)

    # If the form is valid and the method is POST, save the form and redirect
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))  # Redirect to the main product page

    # Pass the form to the template
    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get product by id
    product = get_object_or_404(AddItem, pk=id)
    
    # Delete the product
    product.delete()
    
    # Redirect to the main product page after deletion
    return HttpResponseRedirect(reverse('main:show_main'))