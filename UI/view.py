import flet as ft

import model.corso


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.txt_surname = None
        self.txt_matricola = None
        self.txt_result = None
        self.txt_container = None
        self.ddCorso = None
        self.btn_CercaIscritti = None
        self.btn_CercaStudente = None
        self.btn_CercaCorsi = None
        self.btn_Iscrivi = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        # --1st-- ROW with some controls

        self.ddCorso = ft.Dropdown(
            label="Selezionare un corso",
            width=500,
            options=self.controller.handle_Options()
        )
        self.btn_CercaIscritti = ft.ElevatedButton(
            text="Cerca Iscritti",
            on_click=self._controller.handle_CercaIscritti,
            width=150
        )

        row1 = ft.Row([self.ddCorso, self.btn_CercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # --2nd-- ROW

        # text field for the name
        self.txt_matricola = ft.TextField(
            label="matricola",
            width=150,
            hint_text="Inserisci la tua matricola"
        )
        self.txt_name = ft.TextField(
            label="name",
            width=250,
            read_only=True,
        )
        self.txt_surname = ft.TextField(
            label="surname",
            width=250,
            read_only=True,
        )

        row2 = ft.Row([self.txt_matricola,self.txt_name,self.txt_surname],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # --3rd-- ROW

        self.btn_CercaStudente = ft.ElevatedButton(
            text="Cerca Studente",
            on_click=self._controller.handle_CercaStudente,
            width = 150
        )
        self.btn_CercaCorsi = ft.ElevatedButton(
            text="Cerca Corsi",
            on_click=self._controller.handle_CercaCorsi,
            width = 150
        )
        self.btn_Iscrivi = ft.ElevatedButton(
            text="Iscrivi",
            on_click=self._controller.handle_Iscrivi,
            width= 100
        )

        row3 = ft.Row([self.btn_CercaStudente,self.btn_CercaCorsi,self.btn_Iscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
