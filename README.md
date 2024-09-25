﻿# SHOPIOUS!
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
