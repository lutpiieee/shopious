from django.test import TestCase, Client
from django.utils import timezone
from .models import ReviewItem

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_review_item(self):
        now = timezone.now()
        itemReviewed = ReviewItem.objects.create(
          time = now,
          review = "senang sih, cuman tadi sepatu aku basah kena hujan :(",
          intensity = 8,
        )
        self.assertTrue(itemReviewed.is_mood_strong)