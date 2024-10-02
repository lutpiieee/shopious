﻿﻿# SHOPIOUS!
by Muhammad Luthfi Febriyan - 2306245913
Pengembangan Berbasis Platform 2024/2025
https://pbp.cs.ui.ac.id/muhammad.luthfi39/shopiouss

<details>
<summary> <b> Tugas 2 </b> </summary>

**Langkah-langkah Implementasi Proyek** 
1. menginstal virtual environment `python -m venv env`

2. Aktifkan virtual environment `env\Scripts\activate` 

3. membuat file "requirements.txt" dan mengeditnya menggunakan VS Code untuk menambahkan dependensi yang diperlukan:
```
django 
gunicorn 
whitenoise 
psycopg2-binary 
requests 
urllib3
```

4. install dependensi menggunakan `pip install -r requirements.txt `

5. Membuat proyek Django baru `django-admin startproject shopious . `

6. Setelah proyek terinstal, saya menambahkan "localhost" dan "127.0.0.1" ke daftar ALLOWED_HOSTS di file settings.py. 

7. membuat aplikasi baru bernama main dengan perintah: `python manage.py startapp main` 

8. menambahkan 'main' ke daftar INSTALLED_APPS di file settings.py untuk menandakan kehadiran aplikasi tersebut. 

9. membuat template, saya membuat direktori templates (di dalam direktori main) dan menambahkan file main.html yang akan menjadi template. Saya mengisi template dengan komponen yang diperlukan (nama aplikasi, nama, kelas). 

10. menambahkan model di file models.py bernama Product, yang memiliki atribut name, price, dan description 

11. imigrasikan yang sudah ditambahkan
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
12. mengisi file views.py dengan sebuah fungsi bernama show_main yang akan "mengirimkan" data ke template jika ada permintaan dari template, termasuk app_name, name, dan class.

13. Saya membuat file urls.py di aplikasi main dan menambahkan kode berikut untuk mengonfigurasi routing di aplikasi:
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
Kemudian, saya mengedit urls.py di proyek shopious untuk proyek secara keseluruhan dengan menambahkan:
```
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
]
```

14. membuat repositori baru di GitHub dan menghubungkannya ke repositori lokal dengan menjalankan perintah:
`git init`
Setelah koneksi terbentuk, saya melakukan tindakan add, commit, dan push ke repositori GitHub.
Untuk deployment ke PWS, saya membuat proyek baru bernama 'shopious' di situs PWS, kemudian menambahkan URL deployment PWS saya ke daftar ALLOWED_HOSTS di settings.py.
Akhirnya, saya menghubungkan repositori ke PWS dan melakukan push ke repositori PWS untuk deployment.


**Buatlah bagan**
![image](https://github.com/user-attachments/assets/36e68fa0-7d82-4a56-96fe-a95bb4d91d8d)


**Jelaskan fungsi git dalam pengembangan perangkat lunak!**

Git adalah sistem kontrol versi yang membantu pengembang melacak perubahan pada kode mereka, 
membuat manajemen dan kolaborasi proyek menjadi lebih mudah. Git memungkinkan banyak pengembang bekerja pada proyek yang sama secara bersamaan,
mendukung branching dan merging, serta menyediakan riwayat semua perubahan sehingga memungkinkan pengembalian ke versi sebelumnya jika diperlukan.


**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

salah satu alasan Django dipilih adalah karena menggunakan Python, bahasa yang sudah kita pelajari sejak semester pertama. Ini memungkinkan mahasiswa untuk fokus langsung pada konsep pemrograman berbasis platform tanpa harus mempelajari sintaks baru, karena mereka sudah familiar dengan Python.


**Mengapa model pada Django disebut sebagai ORM?**

Model Django disebut ORM (Object Relational Mapping) karena sifatnya yang langsung mengonversi data menjadi tabel. Akibatnya, pengembang tidak perlu berinteraksi langsung dengan tabel data seperti di SQL, tetapi dapat membuat dan mengakses data langsung dari model.

</details>

<details>
<summary> <b> Tugas 3 </b> </summary>
    
**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
    
Data delivery penting karena memungkinkan komunikasi antara klien, server, dan sistem lain. 
Proses ini memastikan bahwa informasi dapat dikirim dengan cepat, aman, dan efisien. 
Tanpa pengiriman data yang tepat, platform akan terasa lambat dan tidak efisien, yang dapat mengurangi minat pengguna.

**Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

Menurut saya, JSON lebih baik dan lebih populer daripada XML karena struktur JSON lebih sederhana dan mudah dibaca oleh manusia. Selain itu, pemrosesan JSON cenderung lebih cepat dan efisien untuk pertukaran data karena kompleksitasnya lebih rendah dibandingkan dengan XML.

**Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?**

Metode `is_valid()` pada form Django digunakan untuk memeriksa validitas data yang dimasukkan. Jika data yang dimasukkan sesuai dengan persyaratan form (seperti tipe data, panjang data), maka `is_valid()` akan mengembalikan nilai True, jika tidak maka False. Metode ini dibutuhkan untuk memverifikasi dan memastikan bahwa data yang akan dimasukkan ke database sudah benar. Selain itu, metode ini mempermudah penanganan jika terjadi kesalahan pada data yang dimasukkan.

**Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

csrf_token penting untuk melindungi aplikasi web dari serangan Cross-Site Request Forgery (CSRF), di mana penyerang dapat menipu pengguna yang terautentikasi untuk mengirimkan permintaan jahat ke server tanpa sepengetahuan mereka. Tanpa csrf_token, server tidak dapat membedakan antara permintaan yang sah dan yang jahat, sehingga memungkinkan penyerang untuk menyalahgunakan sesi pengguna untuk melakukan tindakan yang tidak diinginkan. Oleh karena itu, csrf_token memastikan bahwa setiap permintaan berasal dari sumber yang sah dan aman.

**IMPLEMENTASI PROGRAM**
1. Menyiapkan Template Pertama, saya membuat folder templates baru di direktori utama dan menambahkan base.html yang berfungsi sebagai tampilan dasar untuk memastikan desain yang konsisten di seluruh situs web dan meminimalkan duplikasi kode.
Untuk menyesuaikan dengan perubahan ini, saya menambahkan `BASE_DIR / 'templates'` di file settings.py ke dalam bagian DIR dari DjangoTemplates.
Kemudian saya menyesuaikan file main.html untuk menggunakan base.html sebagai template utamanya.

2. Membuat Form Input Pertama, saya menambahkan UUID untuk mengidentifikasi setiap review dengan benar dan melakukan migrasi model.
```
class ReviewItem(models.Model):
    ...
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ...
```
3. Kemudian, saya membuat file forms.py yang digunakan untuk membuat struktur form yang dapat menerima entri atau data item baru. File tersebut berisi:
```
from django.forms import ModelForm
from main.models import ReviewItem

class ReviewItemForm(ModelForm):
    class Meta:
        model = ReviewItem
        fields = ["username", "review", "intensity"]
```
4. Di views.py, saya mengimpor redirect dan membuat fungsi baru yang mengimplementasikan form dan memvalidasi input:
```
def create_review_entry(request):
    form = ReviewItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_review_entry.html", context)
```
5. Saya juga memodifikasi fungsi show_main agar dapat menyimpan semua entri:
```
def show_main(request):
    review_entries = ReviewItem.objects.all()

    context = {
    'nama': 'Adidas Samba Nylon Wales Bonner Core Black',
    'harga': 'IDR 7,770,000',
    'deskripsi': 'A few months after the recognizable version, Wales Bonner and adidas reveal a new pack around the legendary Samba model. This Adidas Samba Nylon Wales Bonner Core Black presents a base in black nylon horse dressing, accompanied by a black leather mudguard. The three adidas stripes provide contrast with their white leather design, extending to the heel tab and tongue, marked by the London designer’s touch. A gum sole adds the final touch, preserving the heritage of this iconic soccer shoe.',
    'review_entries': review_entries
    }


    return render(request, "main.html", context)
```
6. Kemudian saya mengimpor fungsi create_review_entry ke dalam urls.py dan mengimplementasikan URL routing dengan menambahkan:
```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-review-entry', create_review_entry, name='create_review_entry'),
    ]
```
7. Saya membuat create_review_entry.html untuk menambahkan halaman HTML untuk mengirimkan entri, yang berisi:
```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Review Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Review Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
8. Kemudian saya memodifikasi main.html untuk menambahkan tombol yang mengarahkan ke pengiriman entri dan menampilkan entri dalam bentuk tabel:
```
    {% if not review_entries %}
      <p style="font-style: italic; color: #999;">There are no reviews for this product yet.</p>
    {% else %}
    <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
      <tr style="background-color: #f5f5f5; text-align: left;">
        <th style="padding: 10px 20px; border-bottom: 1px solid #ddd;">Username</th>
        <th style="padding: 10px 20px; border-bottom: 1px solid #ddd;">Time</th>
        <th style="padding: 10px 20px; border-bottom: 1px solid #ddd;">Review</th>
        <th style="padding: 10px 20px; border-bottom: 1px solid #ddd;">Rating Score</th>
      </tr>
      {% for review_entry in review_entries %}
      <tr>
        <td style="padding: 10px 20px; border-bottom: 1px solid #eee;">{{review_entry.username}}</td>
        <td style="padding: 10px 20px; border-bottom: 1px solid #eee;">{{review_entry.time}}</td>
        <td style="padding: 10px 20px; border-bottom: 1px solid #eee;">{{review_entry.review}}</td>
        <td style="padding: 10px 20px; border-bottom: 1px solid #eee;">{{review_entry.intensity}}</td>
      </tr>
      {% endfor %}
    </table>
    {% endif %}

    <br />
    <a href="{% url 'main:create_review_entry' %}" style="text-decoration: none;">
      <button style="background-color: #333; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 1em; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        Add New Review Entry
      </button>
    </a>
  </div>
</div>

{% endblock content %}
```
9. Menambahkan Tampilan Saya menambahkan 4 fungsi ke dalam views.py untuk mengakses data dalam bentuk XML, JSON, dan berdasarkan ID:
```
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
```
10. Saya mengimpor keempat fungsi tersebut ke urls.py lalu mengimplementasikan URL routing-nya dengan menambahkan:
```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-review-entry', create_review_entry, name='create_review_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```
11. Terakhir, saya menerapkan perubahan yang saya buat ke PWS dan GitHub. Selesai!
</details>

<details>
<summary> <b> Tugas 4 </b> </summary>
    
**Apa perbedaan antara HttpResponseRedirect() dan redirect()**
- HttpResponseRedirect():
  Mengembalikan respons HTTP 302 untuk mengarahkan ke URL yang ditentukan. Berguna jika Anda memerlukan lebih banyak kontrol atas respons sebelum mengembalikannya.
- redirect():
  Menggunakan HttpResponseRedirect() secara internal. Lebih praktis karena dapat menerima berbagai parameter (URL, pola URL yang diberi nama, atau instance model).
  
**Jelaskan cara kerja penghubungan model Product dengan User!**
Cara kerja penghubungan model Product (ReviewEntry) dengan User di Django dilakukan menggunakan ForeignKey. Di dalam Django, hubungan antara dua model dapat diimplementasikan menggunakan relasi database. 
'''
ForeignKey(User, on_delete=models.CASCADE)
'''
Pengguna hanya dapat melihat dan mengelola entri BookEntry yang terkait dengan akun mereka.
Jika pengguna dihapus, semua entri yang terkait dengan pengguna tersebut juga akan dihapus dari database.
Dengan pendekatan ini, Django memastikan bahwa setiap entri produk dikaitkan dengan pengguna tertentu, sehingga data produk dapat dikelola berdasarkan pengguna yang sedang login.

**Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**'
- Authentication: Proses memverifikasi identitas pengguna, seperti memasukkan username dan password.
- Authorization: Menentukan sumber daya atau tindakan yang diizinkan bagi pengguna setelah mereka terautentikasi.

**Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**
Django menggunakan sesi yang disimpan dalam cookies. Setelah login, Django membuat sesi, menyimpan ID sesi, dan mengirimkan cookie sessionid ke browser pengguna.

**IMPLEMENTASI PROGRAM**
1. Aktivasi Virtual Environment: Saya mengaktifkan lingkungan virtual dengan menjalankan perintah:
```
source env/bin/activate
```
2. Mengimpor di views.py:
Mengimpor UserCreationForm untuk mengimplementasikan fungsi register.
AuthenticationForms, authenticate, dan login untuk mengimplementasikan fungsi login.
logout untuk mengimplementasikan fungsi logout.
datetime, HttpResponseRedirect, dan reverse untuk menggunakan cookies.

Kemudian, menambahkan tiga fungsi tersebut (register, login, logout) di file views.py:
```
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
```
```
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
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

3. Menggunakan Cookies:
Menggunakan cookies saat login, maka memodifikasi show_main:
```
def show_main(request):
    ...
                'last_login': request.COOKIES['last_login'],
        }
        return render(request, "main.html", context)
    ...
```

4.File HTML Register dan Login:
Membuat file HTML bernama "register.html" dan "login.html" untuk menampilkan halaman register dan login.
```
#register html
{% extends 'base.html' %}
{% block meta %}
<title>Register</title>
{% endblock meta %}
{% block content %}
<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Register" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>
{% endblock content %}
```
```
#login.html
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
  Tidak punya akun?
  <a href="{% url 'main:register' %}">Daftar Sekarang</a>
</div>
{% endblock content %}
```

5. Logout Button dan Tampilan Last Login di Main Page:
Menambahkan tombol "logout" dan menampilkan data last_login di halaman utama (main.html):
```
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>

<h5>Sesi login terakhir: {{ last_login }}</h5>
```

6. URL Routing:
Mengimpor fungsi register, login, dan logout ke dalam urls.py dan menambahkan path berikut ke urlpatterns:
```
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
```

7. Restriksi Akses untuk Pengguna yang Belum Login:
Memaksa pengguna login sebelum mengakses website, kemudian mengimpor login_required ke dalam views.py dan menambahkan batasan tersebut pada fungsi show_main:
```
@login_required(login_url='/login') #menambahkan diatas fungsi show_main
```

8. Membuat Akun Pengguna dan Data Uji:
Membuat dua akun di halaman saya, yaitu "lutpiieee" dan "ziajam" serta menambahkan beberapa entri review.

9. Menghubungkan Model Product (ReviewEntry) dengan User:
Di models.py, mengimpor User dan memodifikasi kelas ReviewEntry dengan menambahkan:
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Kemudian memodifikasi create_review_entry agar bisa menyimpan user ke database sebelum menyimpan entri review. Saya tidak membuat restriksi bahwa
tiap user tidak bisa melihat review orang lain jadi tidak ada perubahan di show_main
```
    form = ReviewItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        review_entry = form.save(commit=False)
        review_entry.user = request.user
        review_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_review_entry.html", context)
```

10. Migrasi Model
11. Push GitHub dan PWS
</details>

<details>
<summary> <b> Tugas 4 </b> </summary>

    
**IMPLEMENTASI PROGRAM**
- Mengedit data barang
1. Buka views.py yang ada pada subdirektori main, dan buatlah fungsi baru bernama edit_product yang menerima parameter request dan id seperti berikut.
2. Tambahkan import pada file views.py
   ```
   from django.shortcuts import .., reverse
   from django.http import .., HttpResponseRedirect
   ```
3. Buatlah berkas HTML baru dengan nama edit_product.html pada subdirektori main/templates.
4. Buka urls.py yang berada pada direktori main dan import fungsi edit_product yang sudah dibuat dan tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
5. Buka main.html yang berada pada subdirektori main/templates. munculkan tombol edit dan link kan ke edit_product pada setiap baris tabel.


- Menghapus data barang
1. Buat fungsi baru dengan nama delete_product yang menerima parameter request dan id pada views.py di folder main untuk menghapus data product.
2. Buka urls.py yang ada pada folder main dan import fungsi dibuat tadi.
3. Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor.
4. Bukalah berkas main.html yang ada pada folder main/templates dan membuat terdapat tombol hapus untuk setiap produk.

- Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework
1. Menambahkan tailwind ke aplikasi dengan memodifikasi file base.html dengan menambahkan tag <meta name="viewport"> dan <script src="https://cdn.tailwindcss.com">
2. Menambahkan navigation bar pada aplikasi dengan membuat file html baru dinamakan navbar.html
   ```
   <nav class="bg-gray-800 shadow-lg fixed top-2 left-2 z-40 w-screen rounded-lg">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">

        
            <!-- Left Side: Logo -->
            <div class="flex items-center space-x-4">
                <div class="flex-shrink-0">
                    <h1 class="text-2xl font-bold text-white">SHOPIOUS</h1>
                </div>
                
                <!-- Navigation Links -->
                <div class="hidden md:flex space-x-6">
                    <a href="#" class="text-gray-300 hover:text-white">Home</a>
                    <a href="#" class="text-gray-300 hover:text-white">Products</a>
                    <a href="#" class="text-gray-300 hover:text-white">About</a>
                    <a href="#" class="text-gray-300 hover:text-white">Contact</a>
                </div>
            </div>
        
            <!-- Right Side: Welcome and Logout/Login Buttons -->
            <div class="hidden md:flex items-center space-x-4">
                {% if user.is_authenticated %}
                    <span class="text-gray-300">Welcome, {{ user.username }}</span>
                    <a href="{% url 'main:logout' %}" class="ml-4 text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
                        Logout
                    </a>
                {% else %}
                    <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 mr-2">
                        Login
                    </a>
                    <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
                        Register
                    </a>
                {% endif %}
            </div>
    
            <!-- Mobile Menu Button -->
            <div class="md:hidden flex items-center">
                <button class="mobile-menu-button">
                    <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                        <path d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
        </div>
    </div>

    <!-- Mobile Menu -->
    <div class="mobile-menu hidden md:hidden px-4 w-full">
        <div class="pt-2 pb-3 space-y-1">
            <a href="#" class="block text-gray-300 hover:text-white">Home</a>
            <a href="#" class="block text-gray-300 hover:text-white">Products</a>
            <a href="#" class="block text-gray-300 hover:text-white">About</a>
            <a href="#" class="block text-gray-300 hover:text-white">Contact</a>
            {% if user.is_authenticated %}
                <a href="{% url 'main:logout' %}" class="block bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">Logout</a>
            {% else %}
                <a href="{% url 'main:login' %}" class="block bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">Login</a>
                <a href="{% url 'main:register' %}" class="block bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">Register</a>
            {% endif %}
        </div>
    </div>
  
      <script>
        const btn = document.querySelector("button.mobile-menu-button");
        const menu = document.querySelector(".mobile-menu");
  
        btn.addEventListener("click", () => {
            menu.classList.toggle("hidden");
        });
    </script>
   </nav>

   ```
3. Setelah membuat navbar.html, edit product, dan delete product, kemudian konfigurasi static files pada aplikasi dengan memodifikasi settings.py dan menambahkan 'whitenoise.middleware.WhiteNoiseMiddleware' pada bagian MIDDLEWARE. Serta mengubah bagian STATIC_ROOT, TATICFILES_DIRS, dan STATIC_URL.
4. Menambahkan global.css pada folder static/css yang berisi design css. Kemudian saya mengubah base.html agar style global.css dapat digunakan di Django.
5. Modifikasi file login.html, register.html, create_product_entry menjadi styling tailwind. Untuk login.html saya menampilkan static image yang akan ditampilkan sebelah login entry.
6. Membuat file card_product.html yang akan menampilkan card baru untuk setiap product entry baru. Dan di dalam nya ada button untuk edit product dan delete product.
7. Memodifikasi main.html agar segala berkas html lainnya dapat terintegrasi dengan baik.

**Jelaskan urutan prioritas pengambilan CSS selector tersebut!**
Urutannya adalah sebagai berikut:

1. Inline styles
2. ID (#id)
3. Kelas (.class)
4. Selector elemen (div, p, dll.)
   
Selector yang lebih spesifik akan memiliki prioritas lebih tinggi. Jika spesifikasinya sama, urutan penulisan di dalam CSS (cascade) akan berlaku. Selain itu, properti !important akan mengesampingkan semua aturan lainnya, tanpa memandang spesifikasi.

**Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**
Desain responsif sangat penting dalam pengembangan web untuk memastikan bahwa situs web dapat terlihat dan berfungsi dengan baik di berbagai perangkat dan ukuran layar. Desain responsif menggunakan tata letak fleksibel, media queries, dan unit relatif untuk menyesuaikan tampilan di berbagai resolusi.

Contohnya, situs web seperti Amazon atau Tokopedia sudah responsif dan menyesuaikan dengan baik di berbagai perangkat, sementara situs lama atau aplikasi yang kurang terawat mungkin tidak beradaptasi dengan baik, sehingga sulit digunakan di perangkat seluler.

**Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**
Ini adalah properti CSS yang digunakan untuk mengatur jarak di sekitar dan di dalam elemen.

Margin adalah jarak di luar elemen,
Border adalah garis di sekitar kotak elemen, dan
Padding adalah jarak di dalam elemen antara konten dan border.

```
{
  margin: 10px;
  border: 2px solid black;
  padding: 5px;
}
```

**Jelaskan konsep flex box dan grid layout beserta kegunaannya!**
- Flexbox: adalah sistem tata letak satu dimensi (baik horizontal maupun vertikal) yang digunakan untuk mendistribusikan ruang antara item dalam sebuah container, ideal untuk menyusun item dalam baris atau kolom.
- Grid: adalah sistem tata letak dua dimensi yang memungkinkan tata letak lebih kompleks dengan mendefinisikan baris dan kolom.
Flexbox cocok untuk penyesuaian tata letak sederhana dan responsif, sementara Grid lebih unggul dalam menciptakan tata letak yang lebih terstruktur dan menyerupai grid.
</details>