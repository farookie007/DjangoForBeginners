from django.test import TestCase
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
    app_name = None
    view_name = 'home'
    template_path = 'posts/home.html'
    url_location = '/'

    def _generate_reverse_url(self):
        return f"{self.app_name + ':' if self.app_name else ''}{self.view_name}"

    def test_url_exists_by_name(self):
        url = self._generate_reverse_url()
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_by_location(self):
        resp = self.client.get(self.url_location)
        self.assertEqual(resp.status_code, 200)

    def test_view_map_correct_template(self):
        url = self._generate_reverse_url()
        resp = self.client.get(reverse(url))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, self.template_path)

                
    


class AboutPageViewTests(TestCase):
    app_name = None
    view_name = 'about'
    template_path = 'posts/about.html'
    url_location = '/about/'

    def _generate_reverse_url(self):
        return f"{self.app_name + ':' if self.app_name else ''}{self.view_name}"

    def test_url_exists_by_name(self):
        url = self._generate_reverse_url()
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_by_location(self):
        resp = self.client.get(self.url_location)
        self.assertEqual(resp.status_code, 200)

    def test_view_map_correct_template(self):
        url = self._generate_reverse_url()
        resp = self.client.get(reverse(url))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, self.template_path)
