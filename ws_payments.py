# API SOM HÄMTAR UT ORDERNUMMER SOM STATUS FRÅN PAYMENTS

import zeep
from ConnectorDB import insert_order_status, get_connection

conn = get_connection()
wsdl = 'http://localhost:3080/ws/bs.wsdl'

def getPayment(orderId):
    client = zeep.Client(wsdl=wsdl)
    return client.service.getPayment(orderId)
    

for orderId in range(30000, 30500):
    try:
        payment = getPayment(orderId)
        if payment:
            insert_order_status(conn, payment["orderNumber"],payment["status"], payment["amount"], payment["currency"], payment["method"])
    except Exception as e:
        print("something went wrong", e)

conn.close()
