import csv
import matplotlib
from collections import namedtuple

import matplotlib.pyplot as plt

def ParseCsv(fileName:str):

    with open(fileName) as file:
        reader = csv.DictReader(file)
        Row = namedtuple('Row', reader.fieldnames)
        data = tuple(Row(**line) for line in reader)

    return data

Data = ParseCsv("Week-7\Wildfires By Year.csv")
# print(Data)


def GraphData(x, y, xlabel, ylabel, title):
    plt.plot(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.ticklabel_format(useOffset=False, style='plain')

    plt.show() 


def GraphYearsAndAcres():
    x = []
    y = []

    for row in Data:
        x.append(int(row.Year))
        y.append(int(row.Acres))

    x.reverse()
    y.reverse()

    GraphData(x, y, "Year", "Acreage", "Fires Over Years")


def GraphYearsAndFires():
    x = []
    y = []

    for row in Data:
        x.append(int(row.Year))
        y.append(int(row.Fires))

    x.reverse()
    y.reverse()

    GraphData(x, y, "Year", "Fires", "Fires Over Years")

GraphYearsAndFires()
GraphYearsAndAcres()
while(True):
    print("", end="")