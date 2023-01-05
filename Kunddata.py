import json

def kunddata_collector(csv_fil):
    with open(csv_fil, "r") as f:
        rader = f.readlines()
    keys = rader[0].strip().split(",")
    dict_lista = []
    for rad in rader[1:]:
        values = rad.strip().split(",")
        dict = {}
        for i in range(len(keys)):
            dict[keys[i]] = values[i]
        dict_lista.append(dict)
    return dict_lista

#print(kunddata_collector("customers.csv"))  #<--- Okommentera detta för att se resultatet.

def få_topp_tre(json_fil):
    with open(json_fil, 'r') as f:
        json_string = f.read()
    orderinfo = json.loads(json_string)
    amounts = [customer_data['totalAmount'] for customer_id, customer_data in orderinfo.items()]
    amounts.sort(reverse=True)
    
    return amounts[:3]

#print(få_topp_tre("orders.json"))  #<--- Okommentera detta för att se resultatet.