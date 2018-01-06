'''

csv = comma-separated values


import csv

with open('file_name') as csv_var_name:
    var_name = csv.reader(csv_var_name, delimiter=',')

    for var in var_name: ---> rows

'''


import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    dates = []
    colors = []

    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

print(dates)
print(colors)

try:
    whatColor = input('What color do you wish to know the date of? ')

    if whatColor in colors:
        coldex = colors.index(whatColor.lower())
        theDate = dates[coldex]
        print('The date of',whatColor,'is',theDate)
    else:
        print('Color not found, or is not a color!')
# python2: except Exception, e:
except NameError as e:
    print(e)
# (or ---> except Exception as e:)
print('continuing')
