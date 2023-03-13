#!/usr/bin/python CONNECT API TO DATABASE2
import mariadb 

# Modified example from https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/

conn = mariadb.connect(
    user="db_user",
    password="db_user_passwd",
    host="127.0.0.1",
    database="database2")
cur = conn.cursor() 

#retrieving information 
some_name = "Louise" 
cur.execute("SELECT first_name,last_name FROM employees WHERE first_name=?", (some_name,)) 

for first_name, last_name in cur: 
    print(f"First name: {first_name}, Last name: {last_name}")
    
#insert information 
try: 
    cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB"))
    cur.execute("INSERT INTO Desk (employee) VALUES (?)", (cur.lastrowid, )) 
except mariadb.Error as e: 
    print(f"Error: {e}")
    conn.rollback()

conn.commit()
print(f"Last Inserted ID: {cur.lastrowid}")

conn.close()