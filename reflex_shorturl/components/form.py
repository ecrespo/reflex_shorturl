import reflex as rx
from reflex_icons.MaterialDesignIcons import MdInsertLink
from reflex_shorturl.states.formState import FormState


def form_field(
    label: str, placeholder: str, type: str, name: str
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, type=type
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )


def contact_form() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    MdInsertLink(),
                    #rx.icon(tag="link", size=32),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Shorten a long URL",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Enter long link",
                        size="2",
                    ),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field(
                            "Long URL",
                            "Enter long url here",
                            "text",
                            "long_url",
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),

                    rx.form.submit(
                        rx.button("Submit"),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=FormState.handle_submit,
                reset_on_submit=False,
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )