import flet as ft
from view.NavBar import NavBar

def counter_view(page):
    page.title = "Counter"

    nav_bar = NavBar(page)

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def back_home(e):
        page.go("/home")


    return ft.View(
        "/counter",
        controls= [
            ft.Row(
                controls=[
                    ft.IconButton(icon=ft.Icons.REMOVE, on_click=minus_click),
                    txt_number,
                    ft.IconButton(icon=ft.Icons.ADD, on_click=plus_click)
                ]
            ),
            ft.ElevatedButton("Back to home", on_click= back_home)
        ],
        navigation_bar=nav_bar.navigation_bar
    )

