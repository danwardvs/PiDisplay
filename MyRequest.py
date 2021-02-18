import requests
from datetime import datetime
import yfinance as yf

api_key = "OpenWeatherMap_API_KEY_HERE"


def k_to_c(temp):
    return round(temp - 273.15,2)

def request(url):
    try:
        data = requests.get(url,timeout=60)
    except Exception as e:
        print("Error loading " +url)
        return (1,["Error"])
    
    else:
        if data.status_code == 200:
            return (0,data.json())
        else:
            return (1,["Error:" +str(data.status_code)])


def fetch_vaccine():
    result = request("https://api.covid19tracker.ca/summary")
    if result[0] == 0:
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S")

        new_screen = []
        new_screen.append("Total: " + result[1]["data"][0]["total_vaccinations"])
        new_screen.append("Delta: "+result[1]["data"][0]["change_vaccinations"])
        new_screen.append("Dist: "+result[1]["data"][0]["total_vaccines_distributed"])
        new_screen.append(result[1]["last_updated"][5:])
        new_screen.append(dt_string[5:])

        return (0,new_screen)
    else:
        return result

def fetch_weather():
    result = request("http://api.openweathermap.org/data/2.5/weather?q=Woodstock,CA&appid="+api_key)
    if result[0] == 0:

        new_screen = []
        new_screen.append("Temp:  " + str( k_to_c(result[1]['main']['temp'])) + " C")
        new_screen.append("Feels: " + str( k_to_c(result[1]['main']['feels_like'])) + " C")
        print(result[1])
        return (0,new_screen)
    else:
        return result

def fetch_stock(ticker,shares):
    last_quote = 0.0
    try:
        t = yf.Ticker(ticker)
        data = t.history()
        last_quote = (data.tail(1)['Close'].iloc[0])

        if shares == 0:
            return (0,[ticker+': ' + "{:.3f}".format(last_quote)])
        if shares > 0:
            return (0,[ticker+': ' + "{:.3f}".format(last_quote),"Val: $" "{:.2f}".format(last_quote*shares)])

    except Exception as e:
        print("Error fetching " + ticker)
        return (1,["Error pull " + ticker])


