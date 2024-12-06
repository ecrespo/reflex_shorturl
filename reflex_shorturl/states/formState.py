import reflex as rx

from reflex_shorturl.api.api import shorten_url


class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        print(self.form_data)

    @rx.var
    def short_url(self) -> str:
        long_url = self.form_data.get("long_url", "")
        short_url = shorten_url(long_url)
        return short_url