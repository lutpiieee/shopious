import uuid
from django.db import models
from django.contrib.auth.models import User

#membuat models baru untuk add item
class AddItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Pastikan field user ada di sini
    name = models.CharField(max_length=255)  # Nama barang
    photo_url = models.URLField(max_length=500)  # Link for the photo instead of an image upload
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Harga barang
    description = models.TextField()  # Deskripsi barang

    @property
    def is_expensive(self):
        # Check if the price is above a certain threshold
        return self.price > 1000.00
