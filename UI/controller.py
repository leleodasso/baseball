import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._currentTeam = None


    def fillDDanno(self):
        for el in self._model.getAnni():
            self._view._ddAnno.options.append(ft.dropdown.Option(text=el, data=el, on_click=self.onAction))
    def onAction(self, e):
        self._anno = e.control.data
        listaSquadre = self._model.getSquadreAnno(self._anno)
        self._view._txtOutSquadre.clean()
        self._view._txtOutSquadre.controls.append(ft.Text(f"Squadre presenti nell'anno {self._anno}: {len(listaSquadre)}"))
        for squadra in listaSquadre:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{squadra.teamCode} ({squadra.name})"))
        self._view.update_page()

    def fillDDSquadre(self):
        for el in self._model.getNodes():
            self._view._ddSquadra.options.append(ft.dropdown.Option(text=f"{el.teamCode} ({el.name})", data=el, on_click=self.read_dd_team))
        self._view.update_page()

    def read_dd_team(self, e):
        self._currentTeam = e.control.data


    def handleCreaGrafo(self, e):
        self._model.buildGraph(self._anno)
        numNodi, numArci = self._model.getNumeriGrafo()
        self._view._txt_result.clean()
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato con {numNodi} vertici e {numArci} archi"))
        self.fillDDSquadre()
        self._view.update_page()


    def handleDettagli(self, e):
        if self._anno is None or self._currentTeam is None:
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(ft.Text(f"DEVI SELEZIONARE L'ANNO E LA SQUADRA"))
            self._view.update_page()
            return
        listaVicini = self._model.getSquadreVicinePesate(self._currentTeam)
        self._view._txt_result.clean()
        self._view._txt_result.controls.append(ft.Text(f"Adiacenti alla squadra {self._currentTeam.teamCode} ({self._currentTeam.name})"))
        for el in listaVicini:
            self._view._txt_result.controls.append(ft.Text(f"{el[0].teamCode} ({el[0].name})\t\t {el[1]}"))
        self._view.update_page()

    def handlePercorso(self, e):
        pass