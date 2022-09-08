import requests
import json
def intial():
    r=requests.get("http://api.ipify.org").text
    u="https://get.geojs.io/v1/ip/geo/"+r+".json"
    b=requests.get(u)
    k=b.json()
    return k
def get_location():
    b=intial()
    l=b["latitude"]
    f=b["longitude"]
    api_key="283608a9543ccb1dacf7b04382cdb7d4"
    a="http://api.openweathermap.org/geo/1.0/reverse?lat="+l+"&lon="+f+"&limit="+"5"+"&appid="+api_key
    o=requests.get(a)
    k=o.json()
     # r=k["name"]
    # u=k["state"]
    # t="You r in state "+u
    return k
def get_weather():
    k=intial() 
    b=k["latitude"]
    c=k["longitude"]
    d=k["country"]
    api_key="283608a9543ccb1dacf7b04382cdb7d4"
    complete_url = "https://api.openweathermap.org/data/2.5/weather?lat="+b+"&lon="+c+"&appid="+api_key
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404": 
        try: 
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            o="You are in "+b+" in "+c+" State "+" in "+d+" Temperature here (in kelvin unit) is " + str(current_temperature) + "\n atmospheric pressure (in hPa unit) is " + str(current_pressure) + "\n humidity (in percentage) is " + str(current_humidity) + "\n description is " + str(weather_description)
            return o
        except Exception as e:
            a="No idea boss"
            return a
    else:
        return "404 Error"
# print(get_weather())
# print(get_location())