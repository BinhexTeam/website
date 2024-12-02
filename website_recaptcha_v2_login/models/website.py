from odoo import models
from odoo.exceptions import AccessDenied


class Website(models.Model):
    _inherit = "website"

    # --------------------------------------------------
    # METHODS
    # --------------------------------------------------
    """
        Validating that the recaptcha sent is correct
        @params:
            kw: Data sent from the form
    """

    def valid_recaptcha(self, kw):
        valid, message = self.is_recaptcha_v2_valid(kw)
        if not valid:
            raise AccessDenied(message)
        return True
