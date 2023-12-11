import flet as ft


class CustomView(ft.UserControl):

    def __init__(self, route: str, page: ft.Page):

        super().__init__()

        self.page = page
        self.control = ft.View(
            route=route,
            controls=[
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("1")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("2")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("3")
                            ]
                        )
                    ]
                )
            ]
        )

    def build(self):

        return self.control


class CustomAppbar(ft.UserControl):

    def __init__(self):

        super().__init__()
