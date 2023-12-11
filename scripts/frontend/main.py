import flet as ft
from frontend.custom_controls import \
    CustomView


def main(page: ft.Page):

    page.title = "Basic GUI"

    page.views.append(CustomView("test", page=page).build())
    page.update()


ft.app(target=main)
