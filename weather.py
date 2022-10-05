import calendar
import json

# The function should open the filename in read mode and return a dictionary of the JSON decoded contents of the file.
# If the file does not exist, the function should accept the FileNotFoundError and return an empty dictionary.
def read_data(fileName):
    try:
        with open(fileName, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# The function should open the filename in write mode and write the dictionary data into the file encoded as JSON.
def write_data(fileName, data):
    with open(fileName, 'w') as f:
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
            month = calendar.month_name[int(date[4:6])]
            day = str(int(date[6:8]))
            year = str(int(date[0:4]))
            date = month + " " + day + ", " + year
            time = key[8:10] + ":" + key[10:12] + ":" + key[12:14]
            t = data[key]['t']
            h = data[key]['h']
            r = data[key]['r']

            display += f'{month:22}  {time:8}  {t:10}  {h:8}  {r:8}\n'

# The function should return a single string which when passed to any print function will display on the screen formatted exactly as indicated in the example output below. You will most likely be appending strings together using a literal "\n" where a newline is desired. To get the month name, you can import the builtin calendar module and call the month_name function passing it the month as an integer.
def report_historical(data, date):
    # display string
    display = "======================== HISTORICAL REPORT ========================\n"
    display += "Date                      Time  Temperature  Humidity  Rainfall\n"
    display += "====================  ========  ===========  ========  ========\n"
    for key in data:
        if date in key[0:8]:
            month = calendar.month_name[int(date[4:6])]
            day = str(int(date[6:8]))
            year = str(int(date[0:4]))
            date = month + " " + day + ", " + year
            time = key[8:10] + ":" + key[10:12] + ":" + key[12:14]
            t = data[key]['t']
            h = data[key]['h']
            r = data[key]['r']

            display += f'{month:22}  {time:8}  {t:10}  {h:8}  {r:8}\n'


