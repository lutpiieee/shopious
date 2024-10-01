from django.forms import ModelForm
from main.models import AddItem

#menambahkan form baru untuk add item
class addItemForm(ModelForm):
    class Meta:
        model = AddItem
        fields = ["name", "photo_url", "price", "description"] 