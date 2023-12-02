import flet as ft

def main(page: ft.Page):

    page.title = "Basic GUI"

    page.add(
        ft.Row(
            [
                ft.Text("one"),
                ft.Text("two"),
                ft.Text("three")
            ]

        )
    )

ft.app(target=main)
