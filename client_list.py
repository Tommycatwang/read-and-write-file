def main():
    file1 = open('clients.txt','r')
    x = 0
    for reading in file1:
        x=x+1
       
        
        print(x, '.', reading.rstrip('\n'),sep='')
        
    file1.close()
main()