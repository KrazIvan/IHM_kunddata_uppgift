import requests

# function för att få status från Newsletters
def få_status_newsletters():
    api_nyckeln = "70b63d7973cf57ed48c2fd9c2393b228d1db"
    base_url = "http://localhost:3001"
    status_url = f"{base_url}/status"
    headers = {"x-api-key": api_nyckeln}
    svar = requests.get(status_url, headers=headers)

    if svar.status_code == 200:
        # Request lyckades
        data = svar.json()
        print(data)
    else:
        # Request misslyckade
        print(f"Request misslyckades: {svar.status_code}")

if __name__ == "__main__":
    få_status_newsletters()