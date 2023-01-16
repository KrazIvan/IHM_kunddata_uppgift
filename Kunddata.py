from collections import defaultdict
import json

#csv_fil = "customers.csv"
#json_fil = "orders.json"

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

def intkollaren(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def unicodekollaren(fil):
    try:
        with open(fil, "r") as f:
            rader = f.readlines()
            rader[0].strip().split(",")
            return True
    except UnicodeDecodeError:
        return False

def filexistanskollaren(fil):
    try: 
        open(fil, "r")
        return True
    except FileNotFoundError:
        return False

def få_vips(json_fil):
    vip_list_size = input("Hur många köpare vill du se? ")
    while not intkollaren(vip_list_size):
        print("Det där är inte ett giltigt tal. Prova igen.")
        vip_list_size = input("Hur många köpare vill du se? ")
    with open(json_fil, "r") as f:
        json_string = f.read()
    orderinfo = json.loads(json_string)
    amounts = {customer_data["CustomerNumber"]: customer_data["totalAmount"] for customer_id, customer_data in orderinfo.items()}
    sorted_amounts = sorted(amounts.items(), key=lambda x:x[1], reverse=True)
    toppdict = dict(sorted_amounts[:int(vip_list_size)])
    vip_customer_numbers = list(toppdict.keys())
    return [d for d in kunddata_collector(csv_fil) if int(d["CustomerNumber"]) in vip_customer_numbers]

def kund_printer(kunder):
    for d in kunder:
        print(d)

#kund_printer(få_vips(json_fil))  #<--- Okommentera detta för att se resultatet.


def bästa_säljare(json_fil):
    bästa_säljare_list_size = input("Hur lång ska listan vara? ")
    while not intkollaren(bästa_säljare_list_size):
        print("Det där är inte ett giltigt tal. Prova igen.")
        bästa_säljare_list_size = input("Hur lång ska listan vara?  ")
    with open(json_fil) as json_fil:
        säljdata = json.load(json_fil)
    item_data = defaultdict(lambda: {"antal_köp": 0, "inkomst": 0.0})
    for kundnummer, kunddata in säljdata.items():
        for order in kunddata["orders"]:
            for item in order["items"]:
                item_data[item["ean"]]["antal_köp"] += 1
                item_data[item["ean"]]["inkomst"] += item["price"]

    sorted_items = sorted(item_data.items(), key=lambda x: x[1]["antal_köp"] * x[1]["inkomst"], reverse=True)
    bästsäljande = sorted_items[:int(bästa_säljare_list_size)]
    return bästsäljande

def bästsäljande_printer(bästsäljande):
    plats = 1
    for item in bästsäljande:
        print(f"Nummmer {plats} bästsäljande är ean: {item[0]}")
        plats += 1

#bästsäljande_printer(bästa_säljare(json_fil))   #<--- Okommentera detta för att se resultatet.

def minst_aktiva_kunder(json_fil):
    minst_aktiv_kund_lista_storlek = input("Hur lång ska listan vara? ")
    while not intkollaren(minst_aktiv_kund_lista_storlek):
        print("Det där är inte ett giltigt tal. Prova igen.")
        minst_aktiv_kund_lista_storlek = input("Hur lång ska listan vara?  ")
    with open(json_fil, "r") as f:
        json_string = f.read()
    säljdata = json.loads(json_string)
    kunddata = defaultdict(lambda: {"purchases": 0})
    for kundnummer, kund in säljdata.items():
        kunddata[kundnummer]["purchases"] = len(kund["orders"])
    sorterade_kunder = sorted(kunddata.items(), key=lambda x: x[1]["purchases"])
    töntnummer = [kund[0] for kund in sorterade_kunder[:int(minst_aktiv_kund_lista_storlek)]]
    return [d for d in kunddata_collector(csv_fil) if str(d["CustomerNumber"]) in töntnummer]

#kund_printer(minst_aktiva_kunder(json_fil))   #<--- Okommentera detta för att se resultatet.

def kolla_upp_kund(kundnummer):
    for kund in kunddata_collector(csv_fil):
        if kund.get("CustomerNumber") == kundnummer:
            return kund
    return {}

#print(kolla_upp_kund("10004"))   #<--- Okommentera detta för att se resultatet.


def main():
    csv_fil = input("Ange csv-filen, eller ange \"d\" för att använda customers.csv")
    if csv_fil == "d" or csv_fil == "D":
            csv_fil = "customers.csv"
    while not filexistanskollaren(csv_fil) or not unicodekollaren(csv_fil):
        if not filexistanskollaren(csv_fil):
            print("Den här filen finns inte.")
            csv_fil = input("Ange csv-filen.")
            continue
        if not unicodekollaren(csv_fil):
            print("Den här filen kan inte användas.")
            csv_fil = input("Ange csv-filen.")
            continue
    json_fil = input("Ange json-filen, eller ange \"d\" för att använda orders.json")
    if json_fil == "d" or json_fil == "D":
            json_fil = "orders.json"
    while not filexistanskollaren(json_fil) or not unicodekollaren(json_fil):
        if not filexistanskollaren(json_fil):
            print("Den här filen finns inte.")
            json_fil = input("Ange json-filen.")
            continue
        if not unicodekollaren(json_fil):
            print("Den här filen kan inte användas.")
            json_fil = input("Ange json-filen.")
            continue


if __name__ == '__main__':
    main()