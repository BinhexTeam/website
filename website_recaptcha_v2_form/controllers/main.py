import logging

from odoo import _, http
from odoo.exceptions import AccessDenied
from odoo.http import request

from odoo.addons.web.controllers.home import SIGN_UP_REQUEST_PARAMS, Home

logger = logging.getLogger(__name__)


class BinhexHome(Home):
    @http.route("/web/login", type="http", auth="none")
    def web_login(self, redirect=None, **kw):
        Website = request.env["website"].sudo()
        values = {
            k: v for k, v in request.params.items() if k in SIGN_UP_REQUEST_PARAMS
        }
        if request.httprequest.method == "POST":
            request.env["ir.http"]._auth_method_public()
            try:
                valid = Website.get_current_website().valid_recaptcha(kw)
                if valid:
                    return super().web_login(redirect, **kw)
            except AccessDenied as e:
                values.update(
                    {
                        "error": str(
                            e.args[0]
                            if len(e.args) > 0
                            else _("Recaptcha is not valid.")
                        )
                    }
                )
                response = request.render("web.login", values)
                response.headers["X-Frame-Options"] = "SAMEORIGIN"
                response.headers["Content-Security-Policy"] = "frame-ancestors 'self'"
                return response
        return super().web_login(redirect, **kw)
