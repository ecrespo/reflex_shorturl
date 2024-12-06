"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex_shorturl.api.api import hello, shorten_url
from reflex_shorturl.pages.index import index
from rxconfig import config


class State(rx.State):
    """The app state."""
    @rx.var
    def say_hello(self) -> str:
        return hello()





app = rx.App()
#app.add_page(index)
app.api.add_api_route("/hello", hello, methods=["GET"])
app.api.add_api_route("/shorten", shorten_url, methods=["POST"])