from automation.googleSheetsHandler import googleSheetsHandler
import sqlite3

googleSheets = googleSheetsHandler("1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms", "Class Data!A2:E")

connection = sqlite3.connect("rehearsal-hall.db")
cursor = connection.cursor()

currentTime = None # get time format from aero

cursor.execute("""SELECT * 
                    FROM time_logs """)

# WHERE julianday(time_in) is julianday(DATETIME('now', 'localtime'))

rows = cursor.fetchmany()

if rows == None:
    pass
else:
    print(rows)
    pass # call google sheets api and upload to google sheets