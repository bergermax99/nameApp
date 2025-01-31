import flet as ft
from view.NavBar import NavBar

def home_view(page):
    page.title = "Home Sweet Home"

    nav_bar = NavBar(page)

    #    def on_navigation_change(e):
    #       selected_index = e.control.selected_index
    #
    #       if selected_index == 0:
    #          page.go("/home")
    #     elif selected_index == 1:
    #        page.go("/counter")
    #   elif selected_index == 2:
    #      page.go("/todo")

    #    navigation_bar = ft.NavigationBar(
    #        selected_index=0,
    #        on_change=on_navigation_change,
    #        destinations=[
    #            ft.NavigationDestination(icon=ft.Icons.HOME, label="Home"),
    #            ft.NavigationDestination(icon=ft.Icons.ADD, label="Counter"),
    #            ft.NavigationDestination(icon=ft.Icons.HEXAGON_ROUNDED, label="Todo"),
    #
    #        ]
    #   )



    return ft.View(
        route="/home",
        controls=[
            ft.Text("Willkomen auf der Startseite", size=30),
            ft.Text("Das ist die Homeview"),
        ],
        navigation_bar= nav_bar.navigation_bar
    )
