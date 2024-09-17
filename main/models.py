import uuid
from django.db import models

class ReviewItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50)
    time = models.DateField(auto_now_add=True)
    review = models.TextField()
    intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.intensity > 5