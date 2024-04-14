from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, APITestCase
from main import models, api


class TestCreateFamily(APITestCase):

    def setUp(self) -> None:
        self.view = api.FamilyViewset.as_view({'post': 'create'})
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='kuba',
                                             password='kuba')
        self.data = dict(name='Cała kolonia')

    def test_can_create_family_with_founder_member_name(self):
        request = self.factory.post('/families/', self.data)
        request.user = self.user
        self.view(request)
        family = models.Family.objects.get(**self.data)
        self.assertEquals(family.members.first().name, self.user.username)

    def test_founder_member_is_family_boss(self):
        request = self.factory.post('/families/', self.data)
        request.user = self.user
        self.view(request)
        member = models.Member.objects.first()
        self.assertTrue(member.is_boss)

    def test_correct_response_if_ok(self):
        request = self.factory.post('/families/', self.data)
        request.user = self.user
        response = self.view(request)
        self.assertEquals(response.status_code, 201)

    def tearDown(self) -> None:
        return super().tearDown()
