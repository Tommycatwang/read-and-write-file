import csv

infile = open('employeepay.csv','r')
csvfile = csv.reader(infile,delimiter=',')
for reading in csvfile:
    print(reading)