# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
import model.corso as corsi

def get_corsi():
    cnx = get_connection()
    cursor = cnx.cursor(dictionary = True)
    query = """SELECT * FROM corso"""
    cursor.execute(query)
    dicCorsi = {}
    for row in cursor:
        course = corsi.Corso(row["codins"],row["crediti"],row["nome"],row["pd"])
        dicCorsi[row["codins"]] = course
    cursor.close()
    return dicCorsi
def get_corsi_matricola(matricolaStudente):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """SELECT c.* FROM corso c, iscrizione i 
                WHERE c.codins = i.codins AND i.matricola = %s"""
    cursor.execute(query,(matricolaStudente,))
    corsiList = []
    for row in cursor:
        course = corsi.Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
        corsiList.append(course)
    cursor.close()
    return corsiList
def iscriviStudente(corso,matricola):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """INSERT INTO iscrizione (matricola, codins) 
                VALUES (%s,%s);"""
    cursor.execute(query, (matricola,corso))
    cnx.commit()
    cursor.close()
