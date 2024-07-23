from django.test import TestCase
from detector.utils import find_rectangle_corners
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


class UtilsTestCase(TestCase):
    def setUp(self):
        self.test_image_path = './img/img_3.png'

    def test_find_rectangle_corners(self):
        corners = find_rectangle_corners(self.test_image_path)
        self.assertIsInstance(corners, list)
        self.assertEqual(len(corners), 8)


class RectangleDetectViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('rectangle_detect')
        self.test_image_path = './img/img_3.png'
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        response = self.client.post(reverse('token_obtain_pair'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_post_image_path(self):
        data = {"image_path": self.test_image_path}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('points_of_interest', response.data)
        self.assertEqual(len(response.data['points_of_interest']), 8)

    def test_post_no_image_path(self):
        data = {}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('image_path', response.data)
        self.assertEqual(response.data['image_path'][0], 'This field is required.')

    def test_post_invalid_image_path(self):
        data = {"image_path": "./invalid_path/image.png"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
