import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    navbar_link("My URLs", "/#"),
                    navbar_link("Plans", "/#"),
                    navbar_link("Blogs", "/#"),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.text(
                                    "Features",
                                    size="4",
                                    weight="medium",
                                ),
                                rx.icon("chevron-down"),
                                weight="medium",
                                variant="ghost",
                                size="3",
                            ),
                        ),
                        rx.menu.content(
                            rx.menu.item("Service 1"),
                            rx.menu.item("Service 2"),
                            rx.menu.item("Service 3"),
                        ),
                    ),
                    navbar_link("Sign Up", "/#"),
                    navbar_link("Sign In", "/#"),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        # rx.mobile_and_tablet(
        #     rx.hstack(
        #         rx.hstack(
        #             rx.image(
        #                 src="/logo.jpg",
        #                 width="2em",
        #                 height="auto",
        #                 border_radius="25%",
        #             ),
        #             rx.heading(
        #                 "Reflex", size="6", weight="bold"
        #             ),
        #             align_items="center",
        #         ),
        #         rx.menu.root(
        #             rx.menu.trigger(
        #                 rx.icon("menu", size=30)
        #             ),
        #             rx.menu.content(
        #                 rx.menu.item("Home"),
        #                 rx.menu.sub(
        #                     rx.menu.sub_trigger("Services"),
        #                     rx.menu.sub_content(
        #                         rx.menu.item("Service 1"),
        #                         rx.menu.item("Service 2"),
        #                         rx.menu.item("Service 3"),
        #                     ),
        #                 ),
        #                 rx.menu.item("About"),
        #                 rx.menu.item("Pricing"),
        #                 rx.menu.item("Contact"),
        #             ),
        #             justify="end",
        #         ),
        #         justify="between",
        #         align_items="center",
        #     ),
        # ),
        bg=rx.color("accent", 3),
        padding="1em",
        width="100%",
    )