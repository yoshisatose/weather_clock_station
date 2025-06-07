import time
import datetime
import pytz
import requests


# Kallhäll
lon = '17.8061'
lat = '59.4530'
alt = '26'

weather_symbols = {
    1: "Clear sky",
    2: "Nearly clear sky",
    3: "Variable cloudiness",
    4: "Halfclear sky",
    5: "Cloudy sky",
    6: "Overcast",
    7: "Fog",
    8: "Light rain showers",
    9: "Moderate rain showers",
    10: "Heavy rain showers",
    11: "Thunderstorm",
    12: "Light sleet showers",
    13: "Moderate sleet showers",
    14: "Heavy sleet showers",
    15: "Light snow showers",
    16: "Moderate snow showers",
    17: "Heavy snow showers",
    18: "Light rain",
    19: "Moderate rain",
    20: "Heavy rain",
    21: "Thunder",
    22: "Light sleet",
    23: "Moderate sleet",
    24: "Heavy sleet",
    25: "Light snowfall",
    26: "Moderate snowfall",
    27: "Heavy snowfall"
}

def convert_from_UTC_to_Sthlm(dt):
    timezone = 'Europe/Stockholm'
    local_tz = pytz.timezone(timezone)
    return dt.astimezone(tz=local_tz)

def get_forecast():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    res = requests.get(
        'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/%s/lat/%s/data.json'
        % (lon, lat))
    data = res.json()

    approvedTimeUTC = datetime.datetime.fromisoformat(data['approvedTime'])  # UTC
    approvedTime = convert_from_UTC_to_Sthlm(approvedTimeUTC)

    rval = {}
    for hourly_data in data['timeSeries']:
        validTimeUTC = datetime.datetime.fromisoformat(hourly_data['validTime'])
        validTime = convert_from_UTC_to_Sthlm(validTimeUTC)

        hourly_dic = {item['name']: item['values'][0] for item in hourly_data['parameters']}

        print(validTime)
        print(hourly_dic)
        rval.update({
            validTime: {
                'pmean': hourly_dic['pmean'],
                't': hourly_dic['t'],
                'Wsymb2': hourly_dic['Wsymb2']
            }
        })
    return rval
