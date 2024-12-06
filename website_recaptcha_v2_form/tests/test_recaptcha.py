from unittest import mock

from odoo.exceptions import AccessDenied
from odoo.tests import common

imp_requests = "odoo.addons.website_recaptcha_v2.models.website.requests"


class TestModule(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.website = cls.env.ref("website.default_website")
        cls.website.write(
            {
                "recaptcha_v2_enabled": True,
                "recaptcha_v2_site_key": "test-site",
                "recaptcha_v2_secret_key": "test-secret",
            }
        )

    @mock.patch(imp_requests)
    def test_captcha_valid(self, requests_mock):
        requests_mock.post().json.return_value = {"success": True}
        result = self.website.valid_recaptcha(
            {"g-recaptcha-response": "dummy_response"}
        )
        self.assertTrue(result)

    @mock.patch(imp_requests)
    def test_captcha_not_valid(self, requests_mock):
        requests_mock.post().json.return_value = {"success": False}
        with self.assertRaises(AccessDenied):
            self.website.valid_recaptcha({"g-recaptcha-response": ""})

    def test_valid_recaptcha_v2_site_key(self):
        recaptcha_v2_site_key = self.website.recaptcha_v2_site_key
        self.assertEqual(recaptcha_v2_site_key, "test-site")
        recaptcha_v2_site_key = ""
        self.assertNotEqual(
            recaptcha_v2_site_key,
            "test-site",
            msg="The website key for recaptcha is empty.",
        )

    def test_valid_recaptcha_v2_recaptcha_v2_secret_key(self):
        recaptcha_v2_secret_key = self.website.recaptcha_v2_secret_key
        self.assertEqual(recaptcha_v2_secret_key, "test-secret")
        recaptcha_v2_secret_key = ""
        self.assertNotEqual(
            recaptcha_v2_secret_key,
            "test-site",
            msg="The website key for recaptcha is empty.",
        )
