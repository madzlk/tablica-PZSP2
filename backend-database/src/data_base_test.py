import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
#cur.execute("CREATE TABLE test_table(id, name, location)")
#cur.execute("INSERT INTO test_table VALUES (7001, 'Plac politechniki 1', 52.34), (7002, 'Plac politechniki 2', 52.54)")
#con.commit()
res = cur.execute("SELECT * FROM test_table").fetchall()
for i in res:
    for j in i:
        print(type(j))