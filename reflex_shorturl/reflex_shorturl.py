"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex_shorturl.api.api import hello, shorten_url
from reflex_shorturl.components.footer import footer
from reflex_shorturl.components.form import contact_form, FormState
from reflex_shorturl.components.navbar import navbar

from rxconfig import config


class State(rx.State):
    """The app state."""
    @rx.var
    def say_hello(self) -> str:
        return hello()


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.hstack(
            rx.color_mode.button(position="top-right"),
            navbar()
        ),
        rx.vstack(
            rx.heading("Welcome to short URL!", size="9"),
            contact_form(),
            rx.flex(
                rx.text("Shorten URL"),
                rx.link(FormState.short_url, href=FormState.short_url, is_external=True),
                spacing="3",
                flex_direction=[
                    "column",
                    "row",
                    "row",
                ],
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        footer(),
    )


app = rx.App()
app.add_page(index)
app.api.add_api_route("/hello", hello, methods=["GET"])
app.api.add_api_route("/shorten", shorten_url, methods=["POST"])