import flet as ft


class NavBar:
    def __init__(self, page):
        self.page = page
        self.navigation_bar = ft.NavigationBar(
            selected_index=0,
            on_change=self.on_navigation_change,
            destinations=[
                ft.NavigationDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationDestination(icon=ft.Icons.ADD, label="Counter"),
                ft.NavigationDestination(icon=ft.Icons.HEXAGON_ROUNDED, label="Todo"),
                ft.NavigationDestination(icon=ft.Icons.HEXAGON_ROUNDED, label="CUSTOM"),

            ]
        )

    def on_navigation_change(self, e):
        selected_index = e.control.selected_index

        if selected_index == 0:
            self.page.go("/home")
        elif selected_index == 1:
            self.page.go("/counter")
        elif selected_index == 2:
            self.page.go("/todo")
        elif selected_index == 3:
            self.page.go("/custom")

