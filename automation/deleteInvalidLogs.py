import sqlite3
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Connect to the SQLite database
connection = sqlite3.connect(config['DATABASE']['path'])
cursor = connection.cursor()

# Execute DELETE query where the date of `time_in` is the current date

cursor.execute("""DELETE FROM time_logs 
                  WHERE duration_minutes is NULL
                  OR duration_minutes = 0""")

# Commit the changes to the database
connection.commit()

# Close the connection
connection.close()

print("Rows deleted successfully.")
