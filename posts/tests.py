from django.test import TestCase
#from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
from .models import Post

class PostTests(TestCase):
# you find the same keyword from Pythons testing library like unitest
    @classmethod
    def setUpTestData(cls):
        #prepare data for testing later on
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_the_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "posts/home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")