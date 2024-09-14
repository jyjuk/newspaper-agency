from django.contrib.auth import get_user_model
from django.test import TestCase

from newspaper.models import Topic, Newspaper


class ModelsTest(TestCase):
    def test_topics_str(self):
        topic = Topic.objects.create(name="test")
        self.assertEqual(str(topic), topic.name)

    def test_redactor_str(self):
        redactor = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(redactor),
            f"{redactor.username}: "
            f"({redactor.first_name} {redactor.last_name})"
        )

    def test_newspaper_str(self):
        topic = Topic.objects.create(name="test")
        newspaper = Newspaper.objects.create(title="test", topic=topic)
        self.assertEqual(
            str(newspaper),
            f"{newspaper.topic} {newspaper.title}"
        )

    def test_create_redactor_with_experience(self):
        username = "test"
        password = "test123"
        experience = 3
        redactor = get_user_model().objects.create_user(
            username="test",
            password="test123",
            years_of_experience=3
        )
        self.assertEqual(redactor.username, username)
        self.assertTrue(redactor.check_password(password))
        self.assertEqual(redactor.years_of_experience, experience)
