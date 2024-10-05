from automation.googleSheetsHandler import googleSheetsHandler
import sqlite3

googleSheets = googleSheetsHandler("1heMguJXNc2EZncSO7rhVwlQz78iqF54K7-XiYL62I-4", "Logs!A2:D")

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
    
    googleSheetsHandler.insertRows(rows)
    pass # call google sheets api and upload to google sheets