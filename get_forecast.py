# -*- coding: utf-8 -*-
from modules_forecast.smhi_api import get_forecast

import datetime
import pickle
import pytz

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

weather_translation = {
    "Clear sky": "klart",
    "Nearly clear sky": "halvklart",
    "Variable cloudiness": "molnigt",
    "Halfclear sky": "lätt molnighet",
    "Cloudy sky": "mulet",
    "Overcast": "mycket moln",
    "Fog": "dimma",
    "Light rain showers": "lätt regnskur",
    "Moderate rain showers": "regnskur",
    "Heavy rain showers": "kraftig regnskur",
    "Thunderstorm": "åskskur",
    "Light sleet showers": "lätt by av regn och snö",
    "Moderate sleet showers": "ny av regn och snö",
    "Heavy sleet showers": "kraftig by av regn och snö",
    "Light snow showers": "lätt snöby",
    "Moderate snow showers": "snöby",
    "Heavy snow showers": "kraftig snöby",
    "Light rain": "lätt regn",
    "Moderate rain": "regn",
    "Heavy rain": "kraftigt regn",
    "Thunder": "åska",
    "Light sleet": "lätt snöblandat regn",
    "Moderate sleet": "snöblandat regn",
    "Heavy sleet": "kraftigt snöblandat regn",
    "Light snowfall": "lätt snöfall",
    "Moderate snowfall": "snöfall",
    "Heavy snowfall": "ymnigt snöfall"
}

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

try:
    forecast = get_forecast()
#    print(forecast)

    now_hour = datetime.datetime.now().hour

    if now_hour < 12:
    	target = 'today'
    	target_date = datetime.date.today()
    else:
    	target = 'tomorrow'
    	target_date = datetime.date.today() + datetime.timedelta(1)
        
    # Specify the time zone
    stockholm_tz = pytz.timezone('Europe/Stockholm')
    dt_start = datetime.datetime.combine(target_date, datetime.time(hour=8))
    dt_start = stockholm_tz.localize(dt_start)
    dt_end = datetime.datetime.combine(target_date, datetime.time(hour=17))
    dt_end = stockholm_tz.localize(dt_end)

    target_forecast = {key: value for key, value in forecast.items() if key >= dt_start and key <= dt_end}
    print(target_forecast)

    target_weather = [weather_translation[weather_symbols[value['Wsymb2']]] for value in target_forecast.values()]
#    print(target_weather)
    target_temperature = [value['t'] for value in target_forecast.values()]
#    print(target_temperature)

    max_temperature = max(target_temperature)
    min_temperature = min(target_temperature)

    classification = {
        'sunny': ['klart', 'halvklart'],
        'cloudy': ['mulet', 'molnigt', 'dimma', 'mycket moln', 'lätt molnighet'],
        'rain': ['regn', 'lätt regn', 'regnskur', 'kraftigt regn', 'lätt regnskur', 'kraftig regnskur'],
        'snow': ['snöfall', 'lätt snöfall', 'snöby', 'snöblandat regn', 'ymnigt snöfall',
                 'lätt snöby', 'lätt snöblandat regn', 'kraftigt snöblandat regn', 'ny av regn och snö',
                 'kraftig snöby', 'lätt by av regn och snö', 'kraftig by av regn och snö'],
        'thunder': ['åskskur', 'åska']
    }

    count = {}
    for c in classification.keys():
    	count[c] = len([x for x in target_weather if x in classification[c]])
#    print(count)

    target_rain = [value['pmean'] for value in target_forecast.values()]
    rain_max_amount = max(target_rain)
#    print(rain_max_amount)

    weather_summary = {}

    weather_summary['sunny'] = \
        (count['sunny'] >= 3) \
        & (count['rain'] == 0) \
        & (count['snow'] == 0) \
        & (count['thunder'] == 0)

    weather_summary['cloudy_sunny'] = \
        (count['sunny'] < 3) \
        & (count['cloudy'] < 10) \
        & (count['rain'] == 0) \
        & (count['snow'] == 0) \
        & (count['thunder'] == 0)

    weather_summary['cloudy'] = \
        (count['sunny'] == 0) \
        & (count['cloudy'] == 10) \
        & (count['rain'] == 0) \
        & (count['snow'] == 0) \
        & (count['thunder'] == 0)

    weather_summary['rain_sunny'] = \
        (count['sunny'] >= 3) \
        & (count['rain'] > 0) \
        & (count['snow'] == 0) \
        & (count['thunder'] == 0) \
        & (rain_max_amount <= 1)

    weather_summary['rain'] = \
        (count['sunny'] < 3) \
        & (count['rain'] > 0) \
        & (count['snow'] == 0) \
        & (count['thunder'] == 0) \
        & (rain_max_amount <= 1)

    weather_summary['heavy_rain'] = \
        (count['snow'] == 0) \
        & (count['thunder'] == 0) \
        & (rain_max_amount > 1)

    weather_summary['snow_sunny'] = \
        (count['sunny'] >= 3) \
        & (count['snow'] > 0) \
        & (count['thunder'] == 0)

    weather_summary['snow'] = \
        (count['sunny'] < 3) \
        & (count['snow'] > 0) \
        & (count['thunder'] == 0)

    weather_summary['thunder'] = \
        (count['thunder'] > 0)

#    print(weather_summary)

    result = None
    for c in weather_summary.keys():
    	if weather_summary[c]:
    		result = c
    		break

#    print(result)

    # save the result in a file
    rval = {'target': target,
    		'target_forecast': target_forecast,
    		'count': count,
    		'rain_max_amount': rain_max_amount,
    		'weather_summary': weather_summary,
    		'result': result,
    		'max_temperature': max_temperature,
    		'min_temperature': min_temperature}

    pickle.dump(rval, open('data/forecast.pkl', 'wb'))
    print('saved')

except Exception as err:
    print(err)
    rval = {}
    pickle.dump(rval, open('data/forecast.pkl', 'wb'))
