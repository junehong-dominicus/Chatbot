import sqlite3

# DBPATH = "../database.db"
DBPATH = "../example.db"    # make sure - it's from run python folder.

con = sqlite3.connect(DBPATH)
print("Opene databse successfully")

cur = con.cursor()

################################
# # Create table
# cur.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")
#
# # Insert a row of data
# cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#
# # Save (commit) the changes
# con.commit()
# print("Create table, Insert row, and Save(commit) it into databse successfully")
################################

# cur.execute("INSERT INTO stocks VALUES ('2006-03-28', 'BUY', 'IBM', 1000, 45.0)")
# cur.execute("INSERT INTO stocks VALUES ('2006-04-06', 'SELL', 'IBM', 500, 53.0)")
# cur.execute("INSERT INTO stocks VALUES ('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)")
# con.commit()

for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

# Never do this -- insecure!
symbol = 'RHAT'
cur.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol) # How to handle returned cursor oject?

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

################################

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table lang (name, first_appeared)")

# This is the qmark style:
cur.execute("insert into lang values (?, ?)", ("C", 1972))

# The qmark style used with executemany():
lang_list = [
    ("Fortran", 1957),
    ("Python", 1991),
    ("Go", 2009),
]
cur.executemany("insert into lang values (?, ?)", lang_list)

# And this is the named style:
cur.execute("select * from lang where first_appeared=:year", {"year": 1972})
print(cur.fetchall())

con.close()

#############################
import hashlib

def md5sum(t):
    return hashlib.md5(t).hexdigest()

con = sqlite3.connect(":memory:")
con.create_function("md5", 1, md5sum)
cur = con.cursor()
cur.execute("select md5(?)", (b"foo",))
print(cur.fetchone()[0])

con.close()

###############################
class MySum:
    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count

con = sqlite3.connect(":memory:")
con.create_aggregate("mysum", 1, MySum)
cur = con.cursor()
cur.execute("create table test(i)")
cur.execute("insert into test(i) values (1)")
cur.execute("insert into test(i) values (2)")
cur.execute("select mysum(i) from test")
print(cur.fetchone()[0])

con.close()
###############################
