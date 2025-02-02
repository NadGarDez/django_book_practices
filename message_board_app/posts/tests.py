from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.


class PostModelRest(TestCase):
    expected_text = 'blabla'

    def setUp(self):
        Post.objects.create(text=self.expected_text)


    def test_super_model(self):

        post=Post.objects.get(pk=1)
        self.assertEqual(post.text, self.expected_text)
    


class TestHomeView(TestCase):



    def setUp(self):
        Post.objects.create(text = 'Hello World!')

    def test_home_url_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_views_name(self):

        resp = self.client.get(reverse('home'))

        self.assertEqual(resp.status_code, 200)


    def test_views_template(self):

        resp = self.client.get(reverse('home'))

        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'home.html')


