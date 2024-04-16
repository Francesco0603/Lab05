from database import corso_DAO
from database import studente_DAO
class Model:
    def __init__(self):
        self._corsiDict = corso_DAO.get_corsi()
        self._studentiDict = studente_DAO.get_studente()
        self._iscrittiList = None
        self._corsiMatricola = None

    def iscrittiCorso(self,codinsCorso):
        self._iscrittiList = studente_DAO.get_iscritto(codinsCorso)
        return self._iscrittiList
    def corsiMatricola(self,matricolaStudente):
        self._corsiMatricola = corso_DAO.get_corsi_matricola(matricolaStudente)
        return self._corsiMatricola
    def iscrizione(self,matricola,corso):
        corso_DAO.iscriviStudente(corso,matricola)



