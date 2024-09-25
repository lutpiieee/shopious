import uuid
from django.db import models
from django.contrib.auth.models import User


class ReviewItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateField(auto_now_add=True)
    review = models.TextField()
    intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.intensity > 5