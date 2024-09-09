from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Workshirt',
        'price': 'Rp 399.000',
        'description': 'Workshirt dengan bahan fleece'
    }

    return render(request, "main.html", context)