from django.test import TestCase
from django.urls import reverse

from projects.bookversations.models import ReadingList


class ReadingListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ReadingList.objects.create(book_title="Americanah", book_blurb="Ifemelu and Obinze are young and in love when they depart military-ruled Nigeria for the West. Beautiful, self-assured Ifemelu heads for America, where despite her academic success, she is forced to grapple with what it means to be black for the first time. Quiet, thoughtful Obinze had hoped to join her, but with post-9/11 America closed to him, he instead plunges into a dangerous, undocumented life in London. Fifteen years later, they reunite in a newly democratic Nigeria, and reignite their passion—for each other and for their homeland.", book_image="https://images-na.ssl-images-amazon.com/images/I/81fZ4WCGt7L.jpg")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/bookversations')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bookversations:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookversations/index.html')