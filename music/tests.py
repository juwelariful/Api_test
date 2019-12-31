
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
from .models import Songs
from .serializers import SongSerializer

# Create your tests here.

class BaseViewTest(APITestCase):
    client= APIClient()

    @staticmethod
    def create_song(title, artist):
        if title and artist:
            Songs.objects.create(title=title, artist=artist)
    
    def setUp(self):
        self.create_song("like glue", "sean paul")
        self.create_song("simple song", "konshens")
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")

class AllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("song", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Songs.objects.all()
        serialized = SongSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)