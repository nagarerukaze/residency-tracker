import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("rehearsal-hall.db")
cursor = connection.cursor()

# Execute DELETE query where the date of `time_in` is the current date
cursor.execute("""DELETE FROM time_logs 
                  WHERE duration_minutes is NULL""")

# Commit the changes to the database
connection.commit()

# Close the connection
connection.close()

print("Rows deleted successfully.")