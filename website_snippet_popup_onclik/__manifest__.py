{
    "name": "Website Popup Trigger",
    "version": "16.0.1.0.0",
    "author": "Binhex, Odoo Community Association (OCA)",
    "category": "Website",
    "summary": 'Adds an "On Click" trigger option for website popups',
    "website": "https://github.com/OCA/website",
    "license": "AGPL-3",
    "depends": ["web_editor", "website"],
    "data": [
        "views/website_popup_snippet.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "website_snippet_popup_onclik/static/src/js/popup_trigger.js",
        ],
    },
    "installable": True,
    "maintainers": ["arielbarreiros96"],
}
