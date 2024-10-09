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

<details>
<summary> <b> Tugas 6 </b> </summary>

**Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**    
JavaScript adalah bahasa pemrograman esensial dalam pengembangan aplikasi web karena memiliki kemampuan untuk meningkatkan dinamika dan interaktivitas halaman web. Berikut adalah beberapa manfaat utama dari penggunaan JavaScript:

1. Responsivitas dan Interaktivitas
JavaScript memungkinkan halaman web untuk merespons aksi pengguna dengan cepat, mengubah tata letak konten, dan menyediakan pembaruan real-time tanpa perlu memuat ulang seluruh halaman. Hal ini menjadikan aplikasi web terasa lebih dinamis dan sangat meningkatkan pengalaman pengguna.

2. Pemrograman Asinkron
Dengan teknologi seperti AJAX dan fungsi fetch(), JavaScript memungkinkan pemrosesan data dari server secara asinkron, sehingga interaksi dalam aplikasi tidak mengganggu pengalaman pengguna secara keseluruhan.

3. Validasi Input di Sisi Klien
JavaScript memfasilitasi validasi input sebelum data dikirim ke server, mengurangi risiko kesalahan dan mengurangi beban pada backend.

4. Kompatibilitas Lintas Platform
JavaScript mendukung berbagai platform dan browser, memungkinkan aplikasi web dapat diakses dari berbagai perangkat dan sistem operasi tanpa hambatan.

5. Integrasi dengan API Eksternal
JavaScript sangat efektif dalam mengintegrasikan API eksternal, sehingga aplikasi dapat menampilkan data dari sumber lain secara dinamis dan kaya konten.

6. Pengembangan Mobile
JavaScript memudahkan pengembangan lintas platform, memungkinkan pengembang menggunakan satu bahasa pemrograman untuk berbagai platform, baik itu web atau mobile. Framework seperti React Native mendukung pembuatan aplikasi mobile secara efisien dengan basis JavaScript.

**Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?**

Menggunakan await dengan fetch() sangat penting karena akan menunda eksekusi kode hingga promise dari fetch() terselesaikan. Fungsi await memastikan bahwa program menunggu hingga data respons siap digunakan, sehingga mencegah aplikasi melanjutkan eksekusi tanpa data yang diperlukan. Tanpa await, hasil dari fetch() akan berstatus promise yang masih pending, artinya data belum siap diproses. Hal ini dapat menyebabkan variabel yang seharusnya menyimpan data tersebut masih kosong atau tidak terisi dengan benar, sehingga berpotensi menimbulkan kesalahan dalam aplikasi.

Dengan await, alur eksekusi kode lebih jelas karena program menunggu hingga promise dari fetch() terpenuhi. Tanpa await, kode harus bergantung pada metode .then() untuk menangani data yang diterima, yang dapat membuat kode menjadi lebih sulit dibaca dan dikelola. Tanpa await atau .then(), aplikasi mungkin mengalami kesalahan data atau error saat mencoba menggunakan data yang belum tersedia.

**Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?**
Dekorator csrf_exempt digunakan pada permintaan AJAX POST di Django untuk melewati perlindungan CSRF (Cross-Site Request Forgery) ketika token CSRF tidak disertakan dalam permintaan. Hal ini penting karena kode front-end mungkin tidak selalu mengirimkan token CSRF, terutama dalam panggilan AJAX yang langsung berinteraksi dengan server tanpa melalui form yang mengandung token. 

Pengecualian CSRF ini memungkinkan permintaan AJAX untuk diproses, namun penggunaannya harus dilakukan dengan sangat hati-hati karena dapat membuka potensi kerentanan pada aplikasi. Saat menggunakan csrf_exempt langkah-langkah keamanan tambahan harus diterapkan, seperti autentikasi dan validasi input di server, untuk melindungi aplikasi dari serangan CSRF. Jika memungkinkan, disarankan untuk tetap mengirimkan token CSRF dalam permintaan AJAX guna menjaga keamanan dan integritas aplikasi. Selain itu, csrf_exempt sebaiknya digunakan hanya pada endpoint yang benar-benar memerlukan pengecualian, untuk meminimalkan risiko keamanan.

**Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?**

Pembersihan data input pengguna di backend sangat penting dan tidak bisa sepenuhnya digantikan oleh validasi di frontend. Frontend dapat dengan mudah dimanipulasi, misalnya dengan menonaktifkan JavaScript atau menggunakan alat seperti Postman, sehingga backend harus memastikan keamanan dan validitas data sebelum diproses lebih lanjut. Pembersihan di backend juga menjaga integritas data, memastikan semua data yang masuk memenuhi standar yang ditetapkan dan melindungi dari serangan seperti SQL injection atau XSS. Selain itu, backend memungkinkan validasi yang lebih kompleks, seperti pemeriksaan aturan bisnis atau akses database, yang tidak dapat dilakukan di frontend. Ini juga mengurangi beban pada frontend, membuat aplikasi lebih ringan dan responsif. Dengan demikian, pembersihan data di backend tidak hanya meningkatkan keamanan, tetapi juga menjaga kualitas data dan efisiensi aplikasi.

**IMPLEMENTASI PROGRAM**
1. Modifikasi Kode Cards untuk Menggunakan AJAX GET
   ```
   <div id="product_cards"></div>
   dan
     function addItemEntry() {
    const form = document.getElementById('addItemForm');
    fetch("{% url 'main:add_item_entry_ajax' %}", {
        method: "POST",
        body: new FormData(form),
    })
    .then(response => {
        if (response.ok) {
            refreshItemEntries(); // Memperbarui daftar produk setelah berhasil menambah
            form.reset(); // Reset form
            hideModal(); // Tutup modal
        } else {
            console.error('Failed to add item');
        }
    })
    .catch(error => console.error('Error:', error));

    return false; // Mencegah halaman dari refresh
   ```
2. Mengambil Data Menggunakan AJAX GET Pastikan data yang diambil hanya milik pengguna yang sedang login. Kode berikut dalam views.py memastikan bahwa data yang diambil telah difilter untuk pengguna yang login
   ```
   data = Product.objects.filter(user=request.user)
   ```
3. Membuat Tombol untuk Membuka Modal dengan Form untuk Menambahkan Produk Pada file main.html, kita setup modal yang berisi form untuk memasukkan detail produk
```
<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
    <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
      <!-- Modal header -->
      <div class="flex items-center justify-between p-4 border-b rounded-t">
        <h3 class="text-xl font-semibold text-gray-900">Add New Product</h3>
        <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
          <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
          </svg>
          <span class="sr-only">Close modal</span>
        </button>
      </div>
      <!-- Modal body -->
      <div class="px-6 py-4 space-y-6 form-style">
        <form id="addItemForm" action="{% url 'main:create_add_item' %}" method="POST" onsubmit="return addItemEntry();">
          {% csrf_token %}
          <div class="mb-4">
              <label for="name" class="block text-sm font-medium text-gray-700">Product Name</label>
              <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product name" required>
          </div>
          <div class="mb-4">
              <label for="photo_url" class="block text-sm font-medium text-gray-700">Photo URL</label>
              <input type="url" id="photo_url" name="photo_url" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter photo URL" required>
          </div>
          <div class="mb-4">
              <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
              <input type="number" id="price" name="price" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter price" required step="0.01">
          </div>
          <div class="mb-4">
              <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
              <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product description" required></textarea>
          </div>
      </form>
      </div>
      <!-- Modal footer -->
      <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
        <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
        <button type="submit" form="addItemForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
      </div>
    </div>
  </div>
```

4. Untuk membuat tombol yang memicu modal, tambahkan tombol berikut pada main.html:
```
function showModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modal.classList.remove('hidden'); 
      setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
      }, 50); 
  }

  function hideModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modalContent.classList.remove('opacity-100', 'scale-100');
      modalContent.classList.add('opacity-0', 'scale-95');

      setTimeout(() => {
        modal.classList.add('hidden');
      }, 150); 
  }

  document.getElementById("cancelButton").addEventListener("click", hideModal);
  document.getElementById("closeModalBtn").addEventListener("click", hideModal);
```
5. Membuat Fungsi View Baru untuk Menambahkan Produk Baru ke Database dan membuat routing Path yang mengarah ke Fungsi View Baru Tambahkan rute pada urls.py
6. Menyambungkan Form di Dalam Modal ke Path /create-item-ajax/ Buat fungsi ke dalam <script> untuk menyambungkan form dengan path create products ajax
7. Melakukan Refresh Asinkron pada Halaman Utama Tambahkan kode berikut di main.html untuk memuat daftar item terbaru tanpa me-reload seluruh halaman:
```
async function refreshItemEntries() {
    document.getElementById("item_entry_cards").innerHTML = "";
    document.getElementById("item_entry_cards").className = "";
    const itemEntries = await getItemEntries();
    let htmlString = "";
    let classNameString = "";

    if (itemEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
              <img src="{% static 'images/image.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
              <p class="text-center text-gray-600 mt-4">No products available yet.</p>
            </div>
        `;
    }
    else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full";
        itemEntries.forEach((item) => {
            htmlString += `
                <div class="product-card bg-white shadow-md rounded-lg overflow-hidden transition-transform hover:scale-105 duration-300">
                    ${item.fields.photo_url ? `<img src="${item.fields.photo_url}" alt="${item.fields.name}" class="product-image w-full h-48 object-cover rounded-t-lg">` : `<p class="text-center text-gray-400 mb-4">No image available</p>`}
                    <div class="p-6">
                        <h3 class="text-xl font-bold text-gray-900 mb-2">${item.fields.name}</h3>
                        <p class="text-gray-600 text-sm mb-4"><strong>Description:</strong> ${item.fields.description}</p>
                        <p class="text-gray-900 text-lg font-bold"><strong>Price:</strong> ${item.fields.price}</p>
                    </div>
                    <div class="flex justify-between px-6 pb-6">
                        <a href="/edit-product/${item.pk}" class="text-white bg-black py-2 px-4 rounded-lg hover:bg-gray-800 transition">Edit</a>
                        <a href="/delete-product/${item.pk}" class="text-white bg-red-500 py-2 px-4 rounded-lg hover:bg-red-600 transition">Delete</a>
                    </div>
                </div>
            `;
        });
    }
    document.getElementById("item_entry_cards").className = classNameString;
    document.getElementById("item_entry_cards").innerHTML = htmlString;
  }
  refreshItemEntries();  
```
</details>
