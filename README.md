# shopious
shopious 

Tugas 2 
Pengembangan Berbasis Platform 
https://pbp.cs.ui.ac.id/muhammad.luthfi39/shopious 

- Langkah-langkah Implementasi Proyek 
1. menginstal virtual environment 
	python -m venv env 

2. Aktifkan env\Scripts\activate 

3. membuat file "requirements.txt" dan mengeditnya menggunakan VS Code untuk menambahkan dependensi yang diperlukan: 
django 
gunicorn 
whitenoise 
psycopg2-binary 
requests 
urllib3 

4. install dependensi menggunakan 
	pip install -r requirements.txt 

5. Membuat proyek Django baru 
	django-admin startproject shopious . 

6. Setelah proyek terinstal, saya menambahkan "localhost" dan "127.0.0.1" ke daftar ALLOWED_HOSTS di file settings.py. 

7. membuat aplikasi baru bernama main dengan perintah: python manage.py startapp main 

8. menambahkan 'main' ke daftar INSTALLED_APPS di file settings.py untuk menandakan kehadiran aplikasi tersebut. 

9. membuat template, saya membuat direktori templates (di dalam direktori main) dan menambahkan file main.html yang akan menjadi template. Saya mengisi template dengan komponen yang diperlukan (nama aplikasi, nama, kelas). 

10. menambahkan model di file models.py bernama Product, yang memiliki atribut name, price, dan description 

11. imigrasikan yang sudah ditambahkan python manage.py makemigrations python manage.py migrate

12. mengisi file views.py dengan sebuah fungsi bernama show_main yang akan "mengirimkan" data ke template jika ada permintaan dari template, termasuk app_name, name, dan class.

13. Saya membuat file urls.py di aplikasi main dan menambahkan kode berikut untuk mengonfigurasi routing di aplikasi:
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

Kemudian, saya mengedit urls.py di proyek shopious untuk proyek secara keseluruhan dengan menambahkan:
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
]

14. membuat repositori baru di GitHub dan menghubungkannya ke repositori lokal dengan menjalankan perintah:
git init
Setelah koneksi terbentuk, saya melakukan tindakan add, commit, dan push ke repositori GitHub.
Untuk deployment ke PWS, saya membuat proyek baru bernama 'shopious' di situs PWS, kemudian menambahkan URL deployment PWS saya ke daftar ALLOWED_HOSTS di settings.py.
Akhirnya, saya menghubungkan repositori ke PWS dan melakukan push ke repositori PWS untuk deployment.

- Buatlah bagan
+--------------------+     Send HTTP request    +------------------+
|       Client       | -----------------------> |      urls.py     |
+--------------------+                          +------------------+
                                                      |
                                                      v
                                    Directs request to correct view
                                                      |
                                                      v
                                             +------------------+
                                             |     views.py      |
                                             +------------------+
                                                      |
                                       Sends query (interacts with
                                       database through models.py)
                                                      |
                                                      v
                                             +------------------+
                                             |    models.py      |
                                             +------------------+
                                                      ^
                                                      |
                                       Responds with data
                                                      |
                                                      v
+--------------------+ Supplies needed context +------------------+
|      main.html     | <---------------------- |     views.py     |
+--------------------+   to Templates          +------------------+


- Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah sistem kontrol versi yang membantu pengembang melacak perubahan pada kode mereka, membuat manajemen dan kolaborasi proyek menjadi lebih mudah. Git memungkinkan banyak pengembang bekerja pada proyek yang sama secara bersamaan, mendukung branching dan merging, serta menyediakan riwayat semua perubahan sehingga memungkinkan pengembalian ke versi sebelumnya jika diperlukan.

- Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

salah satu alasan Django dipilih adalah karena menggunakan Python, bahasa yang sudah kita pelajari sejak semester pertama. Ini memungkinkan mahasiswa untuk fokus langsung pada konsep pemrograman berbasis platform tanpa harus mempelajari sintaks baru, karena mereka sudah familiar dengan Python.

- Mengapa model pada Django disebut sebagai ORM?
Model Django disebut ORM (Object Relational Mapping) karena sifatnya yang langsung mengonversi data menjadi tabel. Akibatnya, pengembang tidak perlu berinteraksi langsung dengan tabel data seperti di SQL, tetapi dapat membuat dan mengakses data langsung dari model.