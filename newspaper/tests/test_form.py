from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.forms import RedactorCreateForm


class FormTests(TestCase):
    def test_redactor_creation_with_first_last_name_experience_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test First",
            "last_name": "Test Last",
            "years_of_experience": 2,
        }
        form = RedactorCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class PrivateRedactorTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123"
        )
        self.client.force_login(self.user)

    def test_create_redactor(self):
        form_date = {
            "username": "new_user",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test First",
            "last_name": "Test Last",
            "years_of_experience": 5,
        }
        self.client.post(reverse("newspaper:redactor-create"), data=form_date)
        new_user = get_user_model().objects.get(username=form_date["username"])

        self.assertEqual(new_user.first_name, form_date["first_name"])
        self.assertEqual(new_user.last_name, form_date["last_name"])
        self.assertEqual(
            new_user.years_of_experience,
            form_date["years_of_experience"]
        )
