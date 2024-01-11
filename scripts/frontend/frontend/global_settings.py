"""
is used temporarily to simulate config.json
"""

import flet as ft
import json


URL = "http://localhost:8000"

SETTINGS = {
    "general": {
        "color": ft.colors.WHITE
        "bgcolor": ft.colors.GREY_800
    },
    "Button": {
        "color": None
        "bgcolor": None
    },
}


def use_defaults():
    """is used to change unmodified settings to default"""

    pass
