from rest_framework import status
from rest_framework.test import APITestCase
from tags.models import Tag



class TagViewsetTest(APITestCase):
    def setUp(self):
        Tag.objects.create(tag='test', color_text='Importnant', description='test')

    def test_list(self):
        response = self.client.get('/api/tag/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        response = self.client.get('/api/tag/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        tag_data = {'tag': 'test', 'color_text': 'Importnant', 'description': 'test'}
        response = self.client.post('/api/tag/', tag_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Vérification the request values
        response_data = response.data
        self.assertEqual(response_data['tag'], tag_data['tag'])
        self.assertEqual(response_data['color_text'], tag_data['color_text'])
        self.assertEqual(response_data['description'], tag_data['description'])

    def test_update(self):
        updated_tag_data = {'tag': 'updated test', 'color_text': 'Importnant', 'description': 'test'}
        response = self.client.put('/api/tag/1/', updated_tag_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data
        self.assertEqual(response_data['tag'], updated_tag_data['tag'])
        self.assertEqual(response_data['color_text'], updated_tag_data['color_text'])
        self.assertEqual(response_data['description'], updated_tag_data['description'])

    def test_delete(self):
        response = self.client.delete('/api/tag/1/')
        self.assertEqual(response.status_code, 204)
