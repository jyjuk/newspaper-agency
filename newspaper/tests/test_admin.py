from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="test admin"
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="redactor",
            password="test-redactor",
            years_of_experience=3
        )

    def test_redactor_experience_listed(self):
        """
        Test get redactors years_of_experience is
        in list_display on redactor admin page
        :return:
        """
        url = reverse("admin:newspaper_redactor_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)

    def test_redactor_detail_experience_listed(self):
        """
        Test get redactors years_of_experience is on redactor admin page
        :return:
        """
        url = reverse(
            "admin:newspaper_redactor_change",
            args=[self.redactor.id]
        )
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)
