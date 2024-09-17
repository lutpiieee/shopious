from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ReviewItemForm
from main.models import ReviewItem
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    review_entries = ReviewItem.objects.all()

    context = {
    'nama': 'Adidas Samba Nylon Wales Bonner Core Black',
    'harga': 'IDR 7,770,000',
    'deskripsi': 'A few months after the recognizable version, Wales Bonner and adidas reveal a new pack around the legendary Samba model. This Adidas Samba Nylon Wales Bonner Core Black presents a base in black nylon horse dressing, accompanied by a black leather mudguard. The three adidas stripes provide contrast with their white leather design, extending to the heel tab and tongue, marked by the London designer’s touch. A gum sole adds the final touch, preserving the heritage of this iconic soccer shoe.',
    'review_entries': review_entries
    }


    return render(request, "main.html", context)
    
def create_review_entry(request):
    form = ReviewItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_review_entry.html", context)

def show_xml(request):
    data = ReviewItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ReviewItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ReviewItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")    

def show_json_by_id(request, id):
    data = ReviewItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")