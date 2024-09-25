from django.forms import ModelForm
from main.models import ReviewItem

class ReviewItemForm(ModelForm):
    class Meta:
        model = ReviewItem
        fields = ["review", "intensity"]