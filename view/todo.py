from view.task import Task
import flet as ft

class Todo(ft.Column):

    def __init__(self):
        super().__init__()
        self.newTask = ft.TextField(hint_text="Was wollen Sie erledigen?", expand=True)
        self.taskView = ft.Column()
        self.width = 600
        self.controls = [
            ft.Row(
                controls= [
                    self.newTask,
                    ft.FloatingActionButton(icon=ft.Icons.ADD,on_click=self.addClicked),
                ],

            ),
            self.taskView,
        ]


    def addClicked(self, e):
        task = Task(self.newTask.value, self.task_delete)
        self.taskView.controls.append(task)
        self.newTask.value= ""
        self.update()

    def task_delete(self, task):
        self.taskView.controls.remove(task)
        self.update()


