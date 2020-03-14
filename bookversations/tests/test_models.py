from django.test import TestCase

from ..models import NewsletterUser


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all tests methods
        NewsletterUser.objects.create(first_name='Ade', last_name='Coker')

    def test_first_name_label(self):
        user = NewsletterUser.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_first_name_max_length(self):
        user = NewsletterUser.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)