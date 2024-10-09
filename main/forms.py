from django.forms import ModelForm
from main.models import AddItem
from django.utils.html import strip_tags

#menambahkan form baru untuk add item
class addItemForm(ModelForm):
    class Meta:
        model = AddItem
        fields = ["name", "photo_url", "price", "description"] 

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_photo(self):
        photo_url = self.cleaned_data["photo_url"]
        return strip_tags(photo_url)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_desc(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)