import requests  # requests is used to send HTTP requests to the server
from pprint import  pprint  # pprint is used to print the data in a more readable format

API='d862613f3b33985a23a68a1a17cc8192' # Enter the API key from the openweathermap.org

city=input("Enter the city name: ") # input the city name from the user

base_url ="http://api.openweathermap.org/data/2.5/weather?appid="+API+"&q="+city 
 # base url for the api

weather_data=requests.get(base_url).json()  # get the data from the server and convert it into json format

pprint(weather_data)  # print the data in a more readable format