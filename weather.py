import json

<<<<<<< HEAD
import calendar

 

def read_data(filename):

    try:

        with open(filename, 'r') as f:

=======
# The function should open the filename in read mode and return a dictionary of the JSON decoded contents of the file.
# If the file does not exist, the function should accept the FileNotFoundError and return an empty dictionary.
def read_data(filename):
    try:
        with open(filename, 'r') as f:
>>>>>>> d8146b48673aeb710beec1c4abe25f2755151df9
            return json.load(f)

    except FileNotFoundError:

        return {}

<<<<<<< HEAD
 

def write_data(data, filename):

    with open(filename, 'w') as f:

=======
# The function should open the filename in write mode and write the dictionary data into the file encoded as JSON.
def write_data(filename, data):
    with open(filename, 'w') as f:
>>>>>>> d8146b48673aeb710beec1c4abe25f2755151df9
        json.dump(data, f)

 

def max_temperature(data, date):

    x = 0

    for key in data:

        if date == key[0:8]:

            if data[key]['t'] > x:

                x = data[key]['t']

    return x

 

def min_temperature(data, date):

    x = 99999

    for key in data:

        if date == key[0:8]:

            if data[key]['t'] < x:

                x = data[key]['t']

    return x

 

def max_humidity(data, date):

    x = 0

    for key in data:

        if date == key[0:8]:

            if data[key]['h'] > x:

                x = data[key]['h']

    return x

 

def min_humidity(data, date):

    x = 99999

    for key in data:

        if date == key[0:8]:

            if data[key]['h'] < x:

                x = data[key]['h']

    return x

 

def tot_rain( data, date):

    x = 0.0

    for key in data:

        if date == key[0:8]:

            x = x + data[key]['r']

    return x

 

def report_daily(data, date):

    display = "========================= DAILY REPORT ========================\n"

    display = display + "Date                      Time  Temperature  Humidity  Rainfall\n"

    display = display + "====================  ========  ===========  ========  ========\n"

 

    for key in data:
<<<<<<< HEAD

        if date == key[0:8]:

            m = calendar.month_name[int(date[4:6])] + " " + str(int(date[6:8]))+ ", " + str(int(date[0:4]))

            tm = key[8:10] + ":" + key[10:12] + ":" + key[12:14]

=======
        if date in key[0:8]:
            m = calendar.month_name[int(date[4:6])]
            day = str(int(date[6:8]))
            year = str(int(date[0:4]))
            date = m + " " + day + ", " + year
            tm = key[8:10] + ":" + key[10:12] + ":" + key[12:14]
>>>>>>> d8146b48673aeb710beec1c4abe25f2755151df9
            t = data[key]['t']

            h = data[key]['h']

            r = data[key]['r']

<<<<<<< HEAD
            display = display + f'{m:22}{tm:8}{t:13}{h:10}{r:10.2f}' + "\n"

    return display

 

def report_historical(data):

    display = "============================== HISTORICAL REPORT ===========================\n"

    display = display + "                          Minimum      Maximum   Minumum   Maximum     Total\n"

    display = display + "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"

    display = display + "====================  ===========  ===========  ========  ========  ========\n"

 

    d = ''

    for key in data:

        if d == key[0:8]:
=======
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
>>>>>>> d8146b48673aeb710beec1c4abe25f2755151df9

            continue

        else:

            d = key[0:8]

            m = calendar.month_name[int(d[4:6])] + " " + str(int(d[6:8]))+ ", " + str(int(d[0:4]))

            min_temp = min_temperature(data = data, date = d)

            max_temp = max_temperature(data = data, date = d)

            min_hum = min_humidity(data = data, date = d)

            max_hum= max_humidity(data = data, date = d)

            rain = tot_rain(data = data, date = d)

            display = display + f'{m:20}{min_temp:13}{max_temp:13}{min_hum:10}{max_hum:10}{rain:10.2f}' + "\n"

    return display