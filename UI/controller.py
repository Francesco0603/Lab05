import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_CercaIscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        self._view.txt_result.controls.clear()
        corso = self._view.ddCorso.value
        if corso is None or corso == "":
            self._view.create_alert("SELEZIONARE IL CORSO!!")
            return
        self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(self._model.iscrittiCorso(corso))} iscritti al corso:"))
        for iscritto in self._model.iscrittiCorso(corso):
            self._view.txt_result.controls.append(ft.Text(iscritto.__str__()))
        self._view.update_page()

    def handle_CercaStudente(self, e):
        matricola = self._view.txt_matricola.value
        if type(matricola) != int:
            self._view.create_alert("INSERIRE UN Intero Coglione!!")
            return
        print(self._model._studentiDict)
        if matricola is None or matricola == "":
            self._view.create_alert("INSERIRE UNA MATRICOLA!!")
            return
        elif int(matricola) in self._model._studentiDict.keys():
            studente = self._model._studentiDict[int(matricola)]
        else:
            self._view.create_alert("MATRICOLA NON PRESENTE")
            return
        self._view.txt_name.value = studente.nome
        self._view.txt_surname.value = studente.cognome
        self._view.update_page()

    def handle_CercaCorsi(self, e):
        self._view.txt_result.controls.clear()
        matricola = self._view.txt_matricola.value
        if type(matricola) != int:
            self._view.create_alert("INSERIRE UN Intero Coglione!!")
            return
        if matricola is None or matricola == "":
            self._view.create_alert("INSERIRE UNA MATRICOLA!!")
            return
        elif int(matricola) in self._model._studentiDict.keys():
            listaCorsi = self._model.corsiMatricola(int(matricola))
        else:
            self._view.create_alert("STUDENTE ISCRITTO A NESSUN CORSO")
            return
        self._view.txt_result.controls.append(ft.Text(f"Risultano {len(listaCorsi)} corsi:"))
        for corso in listaCorsi:
            self._view.txt_result.controls.append(ft.Text(corso.nome))
        self._view.update_page()

    def handle_Iscrivi(self, e):
        self._view.txt_result.controls.clear()
        matricola = self._view.txt_matricola.value
        if type(matricola) != int:
            self._view.create_alert("INSERIRE UN Intero!!")
            return
        else:
            matricola = int(matricola)
        corso = self._view.ddCorso.value
        if corso is None or corso == "":
            self._view.create_alert("SELEZIONARE IL CORSO!!")
            return
        elif matricola is None or matricola == "":
            self._view.create_alert("INSERIRE UNA MATRICOLA!!")
            return
        elif matricola in self._model._studentiDict.keys():
            if self._model._studentiDict[matricola] in self._model.iscrittiCorso(corso):
                self._view.txt_result.controls.append(ft.Text("Studente già iscritto al corso!"))
            else:
                self._model.iscrizione(matricola,corso)
                self._view.txt_result.controls.append(ft.Text("Iscrizione effettuata!"))
        else:
            self._view.create_alert("STUDENTE NON TROVATO")
            return
        self._view.update_page()

    def handle_Options(self):
        options = []
        for corso in self._model._corsiDict.values():
            options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
        return options


