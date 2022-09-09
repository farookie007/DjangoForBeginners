from django.test import TestCase
from django.urls import reverse

from .models import Post


# Create your tests here.

class PostModelTests(TestCase):
    post_texts = ["Testing 1", "Testing 2", "Testing 3", "Testing 4", "Testing 5", "Pls, work."]
    
    def setUp(self):
        for text in self.post_texts:
            Post.objects.create(text=text)
    
    def test_object_content(self):
        for i, post in enumerate(Post.objects.all()):
            self.assertEqual(self.post_texts[i], post.text)
    
    def test_object_type(self):
        for post in Post.objects.all():
            self.assertEqual(type(post.text), type(''))

        

class HomePageViewTests(TestCase):
    app_name = None
    view_name = 'home'
    template_path = 'posts/home.html'
    url_location = '/'

    def setUp(self):
        self.reverse_url = self._generate_reverse_url()     # generates the reverse url for the `view_name`

    def _generate_reverse_url(self):
        return f"{self.app_name + ':' if self.app_name else ''}{self.view_name}"

    def test_url_exists_by_name(self):
        response = self.client.get(reverse(self.reverse_url))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_by_location(self):
        # test for the url status code from the url route
        resp = self.client.get(self.url_location)
        self.assertEqual(resp.status_code, 200)

    def test_view_map_correct_template(self):
        # test if the 'view_name` maps to the correct template`
        resp = self.client.get(reverse(self.reverse_url))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, self.template_path)
    
    def test_location_match_view(self):
        # test if the `view_name` and `url_location` points to the same view and route
        resp = self.client.get(self.url_location)
        self.assertTemplateUsed(resp, self.template_path)
        resp = self.client.get(reverse(self.reverse_url))
        self.assertTemplateUsed(resp, self.template_path)

class AboutPageViewTests(HomePageViewTests):
    """This test class inherits from HomePageViewTests class since they share similar features"""
    app_name = None
    view_name = 'about'
    template_path = 'posts/about.html'
    url_location = '/about/'
