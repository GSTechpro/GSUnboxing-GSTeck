file= input("enter a file name")
myfile = open(file)
for line in myfile:
    word=line.split()
    for x in word:
        print(x,'#', end=' ')
myfile.close()     
