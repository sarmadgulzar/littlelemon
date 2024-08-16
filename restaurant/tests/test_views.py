from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = self.client.post(
            reverse("api-token-auth"),
            {"username": "testuser", "password": "testpassword"},
        ).json()["token"]
        self.client.defaults.update({"HTTP_AUTHORIZATION": f"Token {self.token}"})
        self.menu_item = Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [MenuSerializer(self.menu_item).data])
