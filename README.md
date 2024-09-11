   s h o p i o u s 
 
Tugas 2 Pengembangan Berbasis Platform
https://pbp.cs.ui.ac.id/muhammad.luthfi39/shopious

Langkah-langkah Implementasi Proyek
1. menginstal virtual environment
   python -m venv env
2. Aktifkan
   env\Scripts\activate
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
7. membuat aplikasi baru bernama main dengan perintah:
   python manage.py startapp main
8. menambahkan 'main' ke daftar INSTALLED_APPS di file settings.py untuk menandakan kehadiran aplikasi tersebut.
9. membuat template, saya membuat direktori templates (di dalam direktori main) dan menambahkan file main.html yang akan menjadi template.
Saya mengisi template dengan komponen yang diperlukan (nama aplikasi, nama, kelas).
10.  menambahkan model di file models.py bernama Product, yang memiliki atribut name, price, dan description
11. imigrasikan yang sudah ditambahkan
   python manage.py makemigrations
python manage.py migrate

