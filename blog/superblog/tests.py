from django.test import TestCase
from django.contrib.auth import get_user_model

from django.test import TestCase

from django.urls import reverse


from .models import Post


# Create your tests here.



class BlogTests(TestCase):

    def setUp(self):

        # first create user instance for testing


        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'abc'
        )
        
        self.post = Post.objects.create(
            title = 'test title',
            body = 'test body',
            author = self.user
        )

    def test_print_method(self):
        post = Post(title = 'title')

        self.assertEqual(str(post), post.title)


    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'test title')
        self.assertEqual(f'{self.post.body}', 'test body')
        self.assertEqual(f'{self.post.author}', 'testuser')


    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Home')

        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/item_page/1/')

        no_response = self.client.get('/item_page/1000/')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(no_response.status_code, 404)
        
    def test_post_create_view(self):
        response = self.client.post(reverse('new_post'),{
            'title':'test title 2',
            'body': 'test body 2'
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test title 2')
        self.assertContains(response, 'test body 2')

    def test_update_view(self):
        response = self.client.post(
            reverse('update_post', args='1'),
            {
                'title': 'updated title'
            }
        )


        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'updated title')

    def test_delete_view(self):
        response = self.client.post(
            reverse('delete_post', args = '1')
        )

        self.assertEqual(response.status_code, 302)





