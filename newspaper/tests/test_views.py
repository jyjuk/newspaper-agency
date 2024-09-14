from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from newspaper.models import Topic

TOPIC_URL = reverse("newspaper:topics-list")


class PublicTopicTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(TOPIC_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_topics(self):
        Topic.objects.create(name="Politics")
        Topic.objects.create(name="Fun")
        response = self.client.get(TOPIC_URL)
        self.assertEqual(response.status_code, 200)
        topics = Topic.objects.all()
        self.assertEqual(list(response.context["topics_list"]), list(topics))
        self.assertTemplateUsed(response, "newspaper/topics_list.html")
