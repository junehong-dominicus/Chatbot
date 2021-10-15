import sqlite3

con = sqlite3.connect(":memory:")
con.isolation_level = None # Controlling Transactions, None for autocommit mode, DEFERRED, IMMEDIATE, or EXCLUSIVE 
cur = con.cursor()

buffer = ""

print("Enter your SQL commands to execute in sqlites.")
print("Enter a blank line to exit.")

while True:
    line = input()
    if line =="":
        break
    buffer += line
    if sqlite3.complete_statement(buffer): # Determine if an SQL statement in buffer is complete.
        try:
            buffer = buffer.strip()
            cur.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print(cur.fetchall())
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        buffer = ""

con.close()
