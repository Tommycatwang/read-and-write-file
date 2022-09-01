import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile,delimiter=',')
write1 = open('customer_country.csv','w')
csvfile2 = csv.writer(write1,delimiter=',')
count11=0
for record in csvfile:
    print(record[0],record[1],record[2],record[3])
    if count11==0:
        write1.write('Full name, country'+'\n')
        count11=count11+1
    else:
        write1.write(record[1] + ' ' +record[2] + ', '+ record[4]+'\n')
        count11=count11+1

write1.write('the total number of customer: ' + str(count11-1))
write1.close()
infile.close()
