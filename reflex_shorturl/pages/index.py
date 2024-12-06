import reflex as rx
from reflex_qrcode import QRCode

from reflex_shorturl.components.footer import footer
from reflex_shorturl.components.form import contact_form
from reflex_shorturl.components.navbar import navbar
from reflex_shorturl.states.formState import FormState
from reflex_shorturl.views.routes import Route
from reflex_shorturl import utils

@rx.page(
    route=Route.INDEX.value,
    title=utils.INDEX_TITLE,
    description=utils.INDEX_DESCRIPTION,
    image=utils.INDEX_IMAGE,
    meta=utils.index_meta
)
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.hstack(
            rx.color_mode.button(position="top-right"),
            navbar()
        ),
        rx.vstack(
            rx.heading("Welcome to short URL!", size="9"),
            rx.hstack(
                contact_form(),
                rx.cond(FormState.short_url != "Error",
                        QRCode(title=f"{FormState.short_url}",value=f"{FormState.short_url}", size=256, level="H")
                ),
            ),
            rx.flex(
                rx.text("Shorten URL:"),
                rx.cond(FormState.short_url == "Error",
                        rx.text("No URL found",color_scheme="red"),
                        rx.link(FormState.short_url, href=f"{FormState.short_url}", is_external=True),
                        ),

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