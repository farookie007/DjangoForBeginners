from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class HomePageViewTests(SimpleTestCase):
    app_name = None
    view_name = 'home'
    template_path = 'home.html'
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

class SignupPageTests(TestCase, HomePageViewTests):
    username = 'testuser'
    email = 'testuser@email.com'
    app_name = None
    view_name = 'signup'
    template_path = 'signup.html'
    url_location = '/users/signup/'
    password = 'secretpass'
    
    def setUp(self):
        super().setUp()
        
        self.payload = {
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
        }

    def test_signup_redirect(self):
        # tests that the response status code is  302 redirect after a successful and
        # valid POST request
        response = self.client.post(reverse(self.reverse_url), self.payload)
        self.assertEqual(response.status_code, 302)

    def test_signup_with_bad_credentials(self):
        # tests that the response status code is 200 after a wrong POST request informations
        # e.g submitting a different password for the confirm password prompt
        # the test ensures that it sends the user back to the signup page instead of redirecting to the home page
        self.payload['password2'] = self.username
        response = self.client.post(reverse(self.
        reverse_url), self.payload)
        self.assertEqual(response.status_code, 200)
    
    def test_user(self):
        get_user_model().objects.create(
            username=self.username,
            email=self.email,
            age=18
        )
        users = get_user_model().objects.all()
        user = users[0]
        self.assertEqual(users.count(), 1)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertEqual(user.age, 18)
