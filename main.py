import flet as ft
from view.homeView import home_view
from view.counterView import counter_view
from view.todoView import todo_view

def main(page: ft.Page):
    page.window.width = 800
    page.window.height = 600

    view_dict = {} # Dictionary werden die Views gespeichert

    def route_change(route):
        page.views.clear()

        if page.route not in view_dict:
            if page.route == "/home":
                view_dict["/home"] = home_view(page)
            elif page.route == "/counter":
                view_dict["/counter"] = counter_view(page)
            elif page.route == "/todo":
                view_dict["/todo"] = todo_view(page)


        page.views.append(view_dict[page.route])
        page.update()



    page.on_route_change = route_change

    page.go("/home")


ft.app(main)