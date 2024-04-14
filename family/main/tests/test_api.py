from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, APITestCase
from main import serializers, models, api


class TestCreateFamily(APITestCase):

    def setUp(self) -> None:
        self.view = api.FamilyViewset.as_view({'post': 'create'})
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='kuba',
                                             password='kuba')
        self.data = dict(name='Cała kolonia')

    def test_can_create_family_with_proper_parameters(self):

        request = self.factory.post('/families/', self.data)
        request.user = self.user
        response = self.view(request)
        print(response.data, response.status_code)
        self.assertEqual(response.status_code, 201)

    def tearDown(self) -> None:
        return super().tearDown()
