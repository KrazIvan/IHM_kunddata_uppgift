import requests

def få_status_newsletters():
    '''
    Function för att få status från Newsletters.

    Output: Status-koden för Newsletters i json-format.
    '''
    api_nyckeln = "70b63d7973cf57ed48c2fd9c2393b228d1db"
    base_url = "http://localhost:3001"
    status_url = f"{base_url}/status"
    headers = {"x-api-key": api_nyckeln}
    svar = requests.get(status_url, headers=headers)

    if svar.status_code == 200:
        # Request lyckades
        data = svar.json()
        return data
    else:
        # Request misslyckades
        return f"Request misslyckades: {svar.status_code}"

if __name__ == "__main__":
    print(få_status_newsletters())