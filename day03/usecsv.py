import csv
import re


def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output


def switchcsv(listname):
    for i in listname:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',', '', j))
            except:
                pass
    return listname
