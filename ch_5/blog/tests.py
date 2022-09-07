from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


# Create your tests here.

class PostModelTests(TestCase):
    posts = [
        {
            'title': "Post 1",
            'body': "Body 1",
        },
        {
            'title': "Post 2",
            'body': "Body 2",
        },
        {
            'title': "Post 3",
            'body': "Body 3",
        },
       {
            'title': "Post 4",
            'body': "Body 4",
        },
       {
            'title': "Post 5",
            'body': "Body 5",
        },
    ]
    
    def setUp(self):
        self.user = get_user_model().objects.create(       # setup the test user
            username = 'testUser',
            email = 'test@email.com',
            password = 'secret_pass'
        )
        for post in self.posts:     # creates the posts for testing
            Post.objects.create(
                title = post['title'],
                body = post['body'],
                author = self.user
            )
        
        self.all_posts = Post.objects.all()     # gets all the post instance in the database
    
    def test_string_representation(self):       # tests if all the posts' string representation is the same as their title
        for i, post in enumerate(self.all_posts):
            self.assertEqual(str(post), self.posts[i]['title'])
    
    def test_post_content(self):
        for i, post in enumerate(self.all_posts):
            self.assertEqual(post.title, self.posts[i]['title'])
            self.assertEqual(post.body, self.posts[i]['body'])
            self.assertEqual(post.author, self.user)
    
    def test_get_absolute_url(self):
        for i, post in enumerate(self.all_posts, 1):
            self.assertEqual(post.get_absolute_url(), f'/post/{i}/')
    
    def test_post_create_view(self):
        post = {
            'title': "New Post",
            'body': "New body",
            'author': self.user,
        }
        response = self.client.post(reverse('post_create'), data=post)
        self.assertEqual(response.status_code, 200)
        for field in post.keys():
            self.assertContains(response, post[field])
    
    def test_post_update_view(self):
        post = {
            'title': "Updated Title",
            'body': "Updated body",
        }
        response = self.client.post(reverse('post_update', kwargs={'pk': 1}), post)
        self.assertEqual(response.status_code, 302)
    
    def test_post_delete_view(self):
        response = self.client.post(
            reverse('post_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)



class BlogListViewTests(TestCase):
    app_name = None
    view_name = 'home'
    template_path = 'blog/home.html'
    url_location = '/'
    url_kwargs = None

    def setUp(self):
        self.reverse_url = self._generate_reverse_url()     # generates the reverse url for the `view_name`

    def _generate_reverse_url(self):
        url = f"{self.app_name + ':' if self.app_name else ''}{self.view_name}"
        return reverse(url, kwargs=self.url_kwargs)

    def test_url_exists_by_name(self):
        response = self.client.get(self.reverse_url)
        self.assertEqual(response.status_code, 200)

    def test_url_exists_by_location(self):
        # test for the url status code from the url route
        resp = self.client.get(self.url_location)
        self.assertEqual(resp.status_code, 200)

    def test_view_map_correct_template(self):
        # test if the 'view_name` maps to the correct template`
        resp = self.client.get(self.reverse_url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, self.template_path)
    
    def test_location_match_view(self):
        # test if the `view_name` and `url_location` points to the same view and route
        resp = self.client.get(self.url_location)
        self.assertTemplateUsed(resp, self.template_path)
        resp = self.client.get(self.reverse_url)
        self.assertTemplateUsed(resp, self.template_path)



class BlogDetailViewTests(BlogListViewTests):
    """This test class inherits from BlogListViewTests class since they share similar methods. It also checks the detail view of the Post model"""
    app_name = None
    view_name = 'post_detail'
    template_path = 'blog/post_detail.html'
    url_kwargs = {'pk': 1}
    post = {
            'title': "Post 1",
            'body': "Body 1",
        }
    
    def setUp(self):
        super().setUp()

        self.url_location = f"/post/{self.url_kwargs['pk']}/"
        self.user = get_user_model().objects.create(       # setup the test user
            username = 'testUser',
            email = 'test@email.com',
            password = 'secret_pass'
        )
        Post.objects.create(
                title = self.post['title'],
                body = self.post['body'],
                author = self.user
            )

    def test_404_error_by_location(self, url_location='/post/1111/'):       # tests a 404 error route to check for NOT FOUND response
        bad_response = self.client.get(url_location)
        self.assertEqual(bad_response.status_code, 404)
    
    def test_404_error_by_name(self):       # tests a 404 error url to check for a NOT FOUND response
        url = f"{self.app_name + ':' if self.app_name else ''}{self.view_name}"
        bad_response = self.client.get(reverse(url, kwargs={'pk':1111}))
        self.assertEqual(bad_response.status_code, 404)
