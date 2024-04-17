import flet as ft
from flet import *
from views.routes import router
from user_controls.app_bar import NavBar

def main(page: ft.Page):

    page.theme_mode = "dark"
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.padding = padding.only(right=100)
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body
    )
    page.go('/hisl')

ft.app(target=main, assets_dir="assets")