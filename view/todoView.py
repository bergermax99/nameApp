import flet as ft
from view.todo import Todo
from view.NavBar import NavBar


def todo_view(page):
    page.title = "Todo App"

    todo = Todo()
    nav_bar = NavBar(page)


    def back_home(e):
        page.go("/home")

    return ft.View(
        "/todo",
        controls = [
            todo,
            ft.ElevatedButton("Back to home", on_click = back_home)
        ],
        horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        navigation_bar=nav_bar.navigation_bar
    )