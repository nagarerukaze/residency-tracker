from automation.googleSheetsHandler import googleSheetsHandler
import sqlite3

googleSheets = googleSheetsHandler("1heMguJXNc2EZncSO7rhVwlQz78iqF54K7-XiYL62I-4", "Logs!A2:D")

connection = sqlite3.connect("rehearsal-hall.db")
cursor = connection.cursor()

currentTime = None # get time format from aero

cursor.execute("""SELECT * 
                    FROM time_logs WHERE DATE(time_in) is DATE('now', 'localtime')""")


rows = cursor.fetchall()

print(rows)

if rows == None:
    pass
else:
    print(rows)
    
    googleSheetsHandler.insertRows(googleSheets, rows)
    pass # call google sheets api and upload to google sheets