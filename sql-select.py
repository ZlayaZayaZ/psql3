import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://lubov:password@localhost:5432/music')
connection = engine.connect()
sel1 = connection.execute("""SELECT name_album, year_of_issue FROM album 
WHERE year_of_issue = 2018;
""").fetchall()
print(sel1)
sel2 = connection.execute("""SELECT name_track, duration FROM track 
ORDER BY duration DESC;
""").fetchone()
print(sel2)
sel3 = connection.execute("""SELECT name_track FROM track
WHERE duration > 210;
""").fetchall()
print(sel3)
sel4 = connection.execute("""SELECT name FROM musician
WHERE name NOT LIKE '%% %%';
""").fetchall()
print(sel4)
sel5 = connection.execute("""SELECT name_collection FROM collection
WHERE year_of_issue BETWEEN 2018 AND 2020;
""").fetchall()
print(sel5)
sel6 = connection.execute("""SELECT name_track FROM track
WHERE name_track LIKE '%%Мой%%' OR name_track LIKE '%%My%%';
""").fetchall()
print(sel6)
