{
    "name": "Website reCAPTCHA v2 form",
    "version": "16.0.1.0.0",
    "category": "Website",
    "depends": ["web", "auth_signup", "website", "website_recaptcha_v2"],
    "author": """
        Binhex,
        Odoo Community Association (OCA)
    """,
    "license": "AGPL-3",
    "website": "https://github.com/OCA/website",
    "summary": "Module to add reCAPTCHA v2 to the login form on the website",
    "data": [
        "views/webclient_templates.xml",
        "views/auth_signup_login_templates.xml",
        "views/s_website_form.xml",
    ],
    "assets": {
        "website.assets_wysiwyg": [
            "website_recaptcha_v2_form/static/src/xml/website_form_editor.xml",
            "website_recaptcha_v2_form/static/src/snippets/s_website_form/options.js",
            "website_recaptcha_v2_form/static/src/snippets/s_website_form/000.js",
        ],
        "web.assets_frontend": [
            "website_recaptcha_v2_form/static/src/css/recaptcha.css",
        ],
    },
    "installable": True,
}
