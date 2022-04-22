import urllib.request
import json
from pop_lookup import population
import pygal

url = "https://api.covid19api.com/summary"
request = urllib.request.urlopen(url)
result = json.loads(request.read())

covid_data = {}

for country in result["Countries"]:
    covid_data[country["CountryCode"]] = country["TotalConfirmed"]

#print(covid_data)

final_data = {}

for key, value in covid_data.items():
    pop = population(key)
    percentage = value / pop * 100
    
    #print(key, round(percentage,2), "%")
    final_data[key] = round(percentage,2)
    

bar_chart = pygal.Bar()
bar_chart.title = 'Country Covid Positivity Rate by %'
for key, value in final_data.items():
    if value > 35:
        bar_chart.add(key, value)
bar_chart.render_to_file('covid.svg')

bar_chart = pygal.Bar()
bar_chart.title = 'Country Covid Positivity Rate by %'
for key, value in final_data.items():
    if value <= 1:
        bar_chart.add(key, value)
bar_chart.render_to_file('low_covid.svg')

wm = pygal.maps.world.World()
o35, o20, u20, o50, o10 = {}, {}, {}, {}, {}
for key, value in final_data.items():
    if value >= 50:
        o50[key.lower()] = value
    elif value >= 35:
        o35[key.lower()] = value
    elif value >= 20:
        o20[key.lower()] = value
    elif value >= 10:
        o10[key.lower()] = value
    else:
        u20[key.lower()] = value

wm.title = 'Country Covid Positivity Rate by %'
wm.add("50% +", o50)
wm.add("35% +", o35)
wm.add("20% +", o20)
wm.add("10% +", o10)
wm.add("Under 10%", u20)

wm.render_to_file('populations.svg')




"""
NOTES:

for key, value in covid_data.items():
    if key == "IN":
        print(key, value)

{'ID': '0581a984-d92a-426b-8022-7c7a2597d97b', 'Country': 'Lithuania', 'CountryCode': 'LT', 'Slug': 'lithuania', 'NewConfirmed': 0, 'TotalConfirmed': 1052417, 'NewDeaths': 0, 'TotalDeaths': 9042, 'NewRecovered': 0, 'TotalRecovered': 0, 'Date': '2022-04-22T17:53:36.359Z', 'Premium': {}}
"""