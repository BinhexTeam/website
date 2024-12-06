import json

from odoo import http
from odoo.tests import new_test_user
from odoo.tests.common import HttpCase

imp_requests = "odoo.addons.website_recaptcha_v2.models.website.requests"


class TestControllerForm(HttpCase):
    def test_url_open(self, data=None, url="/website/form/res.partner"):
        if not data:
            data = {
                "recaptcha_enabled": True,
                "g-recaptcha": "",
            }
        res = self.url_open(
            url=url,
            data=data,
        )
        return res

    def test_recaptcha_enabled_form(self):
        response = self.test_url_open()
        response_recaptcha_invalid = json.loads(response.content.decode("utf-8"))
        self.assertEqual(
            response_recaptcha_invalid.get("error"),
            "No response given.",
            msg=response_recaptcha_invalid.get("error"),
        )
        response_recaptcha_not_enable = self.test_url_open(
            data={"recaptcha_enabled": False}
        )
        self.assertEqual(response_recaptcha_not_enable.status_code, 200)

    def test_recaptcha_enabled_reset_password_login_signup(self):
        new_test_user(self.env, login="test_user", password="Password!1")
        self.authenticate("test_user", "Password!1")
        data = {
            "csrf_token": http.Request.csrf_token(self),
            "g-recaptcha-response": "recaptcha_invalid",
        }

        response_reset = self.test_url_open(url="/web/reset_password", data=data)
        self.assertEqual(response_reset.status_code, 200)

        data.update(
            {
                "login": "test_user",
                "password": "Password!1",
            }
        )
        response = self.test_url_open(url="/web/login", data=data)
        self.assertEqual(response.status_code, 200)
