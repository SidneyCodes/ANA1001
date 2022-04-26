#dataset with the side of the road used in various countries
#this can be used to create some interesting visualizations

import urllib.request
import json


url = "https://restcountries.com/v3.1/all"
request = urllib.request.urlopen(url)
results = json.loads(request.read())

data = {}

for country in results:
    try:
        print(country['capital'])
        data[country["name"]["common"]] = {"country code":country["cca2"],"population":country["population"], "capital":country["capital"],"drives":country["car"]["side"]}
    except:
        pass
    
#print(data)