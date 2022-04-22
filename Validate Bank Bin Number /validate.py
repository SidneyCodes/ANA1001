import requests

def valid(card):
    
    url = f"https://api.apilayer.com/bincheck/{card}"

    payload = {}
    headers= {
      "apikey": ""
    }
    
    response = requests.request("GET", url, headers=headers, data = payload)
    
    status_code = response.status_code
    print(status_code)
    result = response.text
    print(result)
    if status_code == 404:
        return False
    else:
        return True