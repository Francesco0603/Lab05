# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente

def get_studente():
    cnx = get_connection()
    cursor = cnx.cursor(dictionary = True)
    query = """SELECT * FROM studente"""
    cursor.execute(query)
    dicStudenti = {}
    for row in cursor:
        student = Studente(row["matricola"],row["nome"],row["cognome"],row["CDS"])
        dicStudenti[row["matricola"]]= student
    cursor.close()
    return dicStudenti
def get_iscritto(codinsCorso):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary = True)
    query = """SELECT s.* FROM studente s, iscrizione i 
                WHERE i.matricola = s.matricola AND i.codins = %s"""
    cursor.execute(query,(codinsCorso,))
    listaIscritti = []
    for row in cursor:
        student = Studente(row["matricola"],row["nome"],row["cognome"],row["CDS"])
        listaIscritti.append(student)
    cursor.close()
    return listaIscritti


