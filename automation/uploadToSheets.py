import sqlite3

def main():
    
    connection = sqlite3.connect("rehearsal-hall.db")
    cursor = connection.cursor()
    
    currentTime = None # get time format from aero
    
    cursor.execute("""SELECT * 
                      FROM time_logs 
                      WHERE julianday(time_in) is julianday(?)""", (currentTime,))
    
    rows = cursor.fetchmany()
    
    if rows == None:
        pass
    else:
        pass # call google sheets api and upload to google sheets
    
    
if __name__ == "__main__":
    main()