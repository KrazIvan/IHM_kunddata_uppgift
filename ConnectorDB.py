# INGTEGRERA DATA I DATABAS GENOM CONNECTOR
import mariadb 

def get_connection():
    return mariadb.connect(
    user="db_user",
    password="db_user_passwd",
    host="127.0.0.1",
    database="database2")

def insert_order_status(conn, orderNumber, status, amount, currency, method):
    cur = conn.cursor()    
    #SPARA DATA I DATABAS I BEFINTLIG TABELL 
    try: 
        print(orderNumber, status)
        cur.execute("INSERT INTO orderstatus (OrderID,OrderStatus,Amount,Currency,Method) VALUES (?, ?, ?, ?, ?)", (orderNumber, status, amount, currency, method)) 
    except mariadb.Error as e: 
        print(f"Error: {e}")
        conn.rollback()
    conn.commit()
