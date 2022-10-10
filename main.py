from weather import *

myfile = 'w.dat'
choice = 0

while(True):
    print("      *** TUFFY TITAN WEATHER LOGGER MAIN MENU")
    print()
    print("1. Set data FileName")
    print("2. Add Weather Data")
    print("3. Print Daily Report")
    print("4. Print Historical Report")
    print("9. Exit the Program")
    choice = input("Enter menu choice: ")
    print()

    if choice == '1':
        myfile = input("Enter the file name: ")
        weather = read_data(myfile)
    elif choice == '2':
        dt = input("Enter date: ")
        tm = input("Enter time: ")
        t = input("Enter temperature: ")
        h = input("Enter humidity: ")
        r = input("Enter rainfall: ")
        weather[dt + tm] = {'t': t, 'h': h, 'r': r}
        write_data(data = weather, filename = myfile)
    elif choice == '3':
        d = input("Enter date: ")
        display = report_daily(data = weather, date = d)
        print(display)
    elif choice == '4':
        display = report_historical(data = weather)
        print(display)
    elif choice == '9':
        break

