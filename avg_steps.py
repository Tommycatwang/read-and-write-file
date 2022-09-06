import csv

infile = open('steps.csv','r')

csvfile = csv.reader(infile,delimiter=',')
write1 = open('avg_steps.csv','w')
csvfile2 = csv.writer(write1,delimiter=',')
next(csvfile)
count11=0
count22=0
mon_inyear = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
x=0
for record in csvfile:
    
    print(int(record[0]),record[1],)
    
    if int(record[0])== x or x == 0:
        count11=count11 + int(record[1])
        count22=count22 + 1
        x = int(record[0])
    else:
        count11=count11/count22
        count22=0
        monthinna= mon_inyear[x-1]
        format_two="{:.2f}".format(count11)
        write1.write(monthinna + ', ' + str(format_two) +'\n')
        x=0
        count11=int(record[1])
count11=count11/count22
count22=0
monthinna= mon_inyear[x-1]
format_two="{:.2f}".format(count11)
write1.write(monthinna + ', ' + str(format_two) +'\n')
write1.close()
infile.close()
