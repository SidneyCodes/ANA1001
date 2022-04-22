import urllib.request
import json

def population(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code}"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    
    population = result[0]["population"]
    print("Finished with",country_code)
    
    #print(f"{population:,}")

    return population
    
    #https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators