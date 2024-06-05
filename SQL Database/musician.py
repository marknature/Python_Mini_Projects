import sqlite3

con = sqlite3.connect('musician.sqlite')
cur = con.cursor()
# cur.execute("CREATE TABLE Tracks (Firstname text, surname text, age int);")
cur.execute("INSERT INTO Tracks VALUES ('King', 'Kong', '30');")
cur.execute("INSERT INTO Tracks VALUES ('Silent', 'K', '20');")
cur.execute("INSERT INTO Tracks VALUES ('K', 'G', '3');")
cur.execute("INSERT INTO Tracks VALUES ('Kig', 'Kg', '45');")
cur.execute("Select * from Tracks;")
result = cur.fetchall()

cur.close()
