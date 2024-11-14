odoo.define("website_snippet_popup_onclik.s_popup_options", function (require) {
    "use strict";

    const options = require("web_editor.snippets.options");

    options.registry.SnippetPopup = options.Class.extend({
        start: function () {
            this._super.apply(this, arguments);
            console.log("SnippetPopup logic initialized");
        },

        /**
         * Custom handler for "On Click" option.
         */
        onClickOptionHandler: function () {
            console.log("On Click option triggered");
            this._bindClickEvent();
        },

        /**
         * Bind click event to the trigger button that shows the popup.
         */
        _bindClickEvent: function () {
            const button = document.querySelector(
                'button[data-popup-action="triggerOnClick"]'
            );
            if (button) {
                button.addEventListener("click", (event) => {
                    event.preventDefault();
                    console.log("Popup trigger button clicked");
                    this._showPopup();
                });
            }
        },

        /**
         * Function to show the popup when triggered.
         */
        _showPopup: function () {
            const popupElement = document.querySelector(".s_popup");
            if (popupElement) {
                $(popupElement).modal("show");
                console.log("Popup displayed");
            }
        },
    });
});
