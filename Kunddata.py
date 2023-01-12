import json

csv_fil = "customers.csv"
json_fil = "orders.json"

def kunddata_collector(csv_fil):
    with open(csv_fil, "r") as f: # 'r' betyder att man läser in filen.
        rader = f.readlines()
    keys = rader[0].strip().split(",")
    dict_lista = []
    for rad in rader[1:]:
        values = rad.strip().split(",")
        dict = {}
        for i in range(len(keys)):
            dict[keys[i]] = values[i]
        dict_lista.append(dict)
    return dict_lista # retunerar en dict.

#print(kunddata_collector("customers.csv"))  #<--- Okommentera detta för att se resultatet.

def intkollaren(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def få_vips(json_fil):
    vip_list_size = input("Hur många köpare vill du se? ")
    while not intkollaren(vip_list_size):
        print("Det där är inte ett giltigt tal. Prova igen.")
        vip_list_size = input("Hur många köpare vill du se? ")
    with open(json_fil, 'r') as f:
        json_string = f.read()
    orderinfo = json.loads(json_string)
    amounts = {customer_data["CustomerNumber"]: customer_data['totalAmount'] for customer_id, customer_data in orderinfo.items()}
    sorted_amounts = sorted(amounts.items(), key=lambda x:x[1], reverse=True)
    toppdict = dict(sorted_amounts[:int(vip_list_size)])
    vip_customer_numbers = list(toppdict.keys())
    return [d for d in kunddata_collector(csv_fil) if int(d["CustomerNumber"]) in vip_customer_numbers]

def vip_printer(vips):
    for d in vips:
        print(d)

vip_printer(få_vips(json_fil))  #<--- Okommentera detta för att se resultatet.