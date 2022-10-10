import calendar
import json

# The function should open the filename in read mode and return a dictionary of the JSON decoded contents of the file.
# If the file does not exist, the function should accept the FileNotFoundError and return an empty dictionary.
def read_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# The function should open the filename in write mode and write the dictionary data into the file encoded as JSON.
def write_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

# The function should return the maximum temperature for all dictionary data where the key contains the date as YYYYMMDD.
def max_temperature(data, date):
    maxTemp = 0
    for key in data:
        if date in key[0:8]:
            if data[key]['t'] > maxTemp:
                maxTemp = data[key]['t']
    return maxTemp

# The function should return the minimum temperature for all dictionary data where the key contains the date as YYYYMMDD.
def min_temperature(data, date):
    minTemp = 999
    for key in data:
        if date in key[0:8]:
            if data[key]['t'] < minTemp:
                minTemp = data[key]['t']
    return minTemp

# The function should return the maximum humidity for all dictionary data where the key contains the date as YYYYMMDD.
def max_humidity(data, date):
    maxHum = 0
    for key in data:
        if date in key[0:8]:
            if data[key]['h'] > maxHum:
                maxHum = data[key]['h']
    return maxHum

# The function should return the minimum humidity for all dictionary data where the key contains the date as YYYYMMDD.
def min_humidity(data, date):
    minHum = 999
    for key in data:
        if date in key[0:8]:
            if data[key]['h'] < minHum:
                minHum = data[key]['h']
    return minHum

# The function should return the sum of rainfall for all dictionary data where the key contains the date as YYYYMMDD.
def tot_rain(data, date):
    totRain = 0
    for key in data:
        if date in key[0:8]:
            totRain += data[key]['r']
    return totRain

# The function should return a single string which when passed to any print function will display on the screen formatted exactly as indicated in the example output below. You will most likely be appending strings together using a literal "\n" where a newline is desired. To get the month name, you can import the builtin calendar module and call the month_name function passing it the month as an integer.
def report_daily(data, date):
    # display string
    display = "========================= DAILY REPORT ========================\n"
    display += "Date                      Time  Temperature  Humidity  Rainfall\n"
    display += "====================  ========  ===========  ========  ========\n"
    for key in data:
        if date in key[0:8]:
            m = calendar.month_name[int(date[4:6])]
            day = str(int(date[6:8]))
            year = str(int(date[0:4]))
            date = m + " " + day + ", " + year
            tm = key[8:10] + ":" + key[10:12] + ":" + key[12:14]
            t = data[key]['t']
            h = data[key]['h']
            r = data[key]['r']

            display += f'{date<22}'+ f'{tm<8}'+ f'{t>13}'+ f'{h>10}'+ f'{r>10}\n'

# The function should return a single string which when passed to any print function will display on the screen formatted exactly as indicated in the example output below. You will most likely be appending strings together using a literal "\n" where a newline is desired. To get the month name, you can import the builtin calendar module and call the month_name function passing it the month as an integer.
def report_historical(data):
    # display string
    display = "======================== HISTORICAL REPORT ========================\n"
    display += "			  Minimum      Maximum   Minimum   Maximum     Total\n"
    display += "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    display += "====================  ===========  ===========  ========  ========  ========\n"

    h = ''

    for key in data:
        if h == key[0:8]:
            continue
        else:
            h = key[0:8]
            m = calendar.month_name[int(h[4:6])]
            day = str(int(h[6:8]))
            year = str(int(h[0:4]))
            date = m + " " + day + ", " + year
            
            min_temp = min_temperature(data, h)
            max_temp = max_temperature(data, h)
            min_hum = min_humidity(data, h)
            max_hum = max_humidity(data, h)
            rain = tot_rain(data, h)

            display += f'{date:22}'+ f'{min_temp:10}'+ f'{max_temp:10}'+ f'{min_hum:8}'+ f'{max_hum:8}'+ f'{rain:8}\n'


