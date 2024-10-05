from googleSheetsHandler import googleSheetsHandler
import sqlite3
import configparser

config = configparser.ConfigParser()
config.read('./config.ini')

googleSheets = googleSheetsHandler(config.get("SHEETS", "id"), config.get("SHEETS", "range"))

connection = sqlite3.connect(config.get("DATABASE", "path"))
cursor = connection.cursor()

currentTime = None # get time format from aero

cursor.execute("""SELECT * 
                    FROM time_logs 
                    WHERE DATE(time_in) is DATE('now', 'localtime')
                    """)

# AND duration_minutes IS NOT NULL

rows = cursor.fetchall()

if rows == None:
    pass
else:
    print(rows)
    googleSheetsHandler.insertRows(googleSheets, rows)
    pass