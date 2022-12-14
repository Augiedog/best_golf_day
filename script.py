import pprint
import requests
from matplotlib import pyplot as plt
from datetime import datetime

# here we are formatting the PrettyPrinter. Try using different indents!
pp = pprint.PrettyPrinter(indent=3)

API_URL = 'https://goweather.herokuapp.com/weather/'
city = 'seatle' 
r = requests.get(API_URL + city)
response = r.json()
# The return from the api dressed up for the counsole
pp.pprint(response)

# adds date in front of response
forecast_list = response['forecast']
today = datetime.now().strftime("%b-%d-%Y")


to_graph = {} # The empty dictionary to store our shaped data
count = 1 # A global iterator to track each day past current datetime

for day in forecast_list:
    current_date = int(today[4:6]) + count
    this_day = f"{today[0:4]}{current_date}{today[6:]}"
    count += 1

    to_graph[this_day] = day['wind']
pp.pprint(to_graph)

# expected output should look something like:
#   {'Aug-24-2021': 12,
#    'Aug-25-2021': 14,  
#    'Aug-26-2021': 0 }


# Remember to always label the axes of your graph!
plt.xlabel('Date')
plt.ylabel('Wind')
# plt.ylabel('Temperature')

print('to_graph keys: ', to_graph.keys())
print('to_graph values: ', to_graph.values())

plt.scatter(to_graph.keys(), to_graph.values()) # sets up the graph
plt.show() # paints the graph to your screen


# Currently, if we were to start a search on one of the last 2 days of the month, our dates will look screwy, potentially going beyond the confines of agreed-upon datetime. How could you resolve the edge-cases that could cause these errors?
# Try adapting our script to display a bar graph of the temperatures of the next three days
# Sometimes the API returns unclean data, looking like: ' km / h' for the wind speed on any given day. Adapt your code to handle this event. Assume if wind speed is not posted, the wind speed will be 0.
