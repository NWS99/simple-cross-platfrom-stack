import flet as ft
from frontend.global_settings import SETTINGS


class UniformView(ft.UserControl):

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
                                ft.Text(
                                    "1", 
                                    color=SETTINGS["general"]["color"]
                                )
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


class UniformAppbar(ft.UserControl):

    def __init__(self):

        super().__init__()


class UniformButton(ft.UserControl):

    def __init__(self):

        super().__init__()


class UniformContainer(ft.UserControl):

    def __init__(self):

        super().__init__()
