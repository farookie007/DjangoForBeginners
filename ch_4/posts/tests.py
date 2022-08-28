from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from .models import Post

# Create your tests here.

class PostModelTests(TestCase):
    post_text = "Pls, work."
    
    def setUp(self):
        Post.objects.create(text=self.post_text)

    def get_post_content(self):
        post = Post.objects.get(id=1)
        return post.text
    
    def test_object_content(self):
        content = self.get_post_content()
        self.assertEqual(content, self.post_text)
    
    def test_object_type(self):
        content = self.get_post_content()
        self.assertEqual(type(content), type(''))


class HomePageViewTests(TestCase):
    def test_url_exists(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_url_exists_by_name(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


class AboutPageViewTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
    
    def test_url_exists_by_name(self):
        resp = self.client.get('/about/')
        self.assertEqual(resp.status_code, 200)
