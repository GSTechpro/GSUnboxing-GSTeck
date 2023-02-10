#question 1
file= input("enter a file name")
myfile = open(file)
for line in myfile:
    word=line.split()
    for x in word:
        print(x,'#', end=' ')
myfile.close()        

print ("<><><><><><><><><><><>><><><><><><><><><><><><><><><><>><><><><><><><><><><<><>")

#question 2
def countvcul():
      f=open("twinkle.txt",'r')
      v=c=u=l=0
      data=f.read()
      for i in data :
            if i.isupper():
                  u+=1
            if i.islower():
                  l+=1
            if i.lower() in 'aeiou':
                  v+=1
            else:
                  c+=1
      print("vowels are...",v)
      print("consonants are...",c)
      print("uppercase charecters are...",u)
      print("lowercase charecters are...",l)
countvcul()                           

print ("<><><><><><><><><><><>><><><><><><><><><><><><><><><><>><><><><><><><><><><<><>")

#question 3
def remove():
  f=open("sampleold.txt",'r')
  lines=f.readlines()
  fo=open("sampleold.txt",'w')
  fn=open("samplenew.txt",'w')
  for line in lines:
    if 'a' in line:    
      fn.write(line)
    else:
      fo.write(line) 
print("data updated in sampleold file and crated samplenew file created also....")
remove()                                
                  
print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><<><><><><><><><>")

#question4                  
import pickle
def  Writerecord(sroll,sname):
   with open ('StudentRecord1.dat','ab') as Myfile:
       srecord={"SROLL":sroll,"SNAME":sname}
       pickle.dump(srecord,Myfile)

     

def Readrecord():
   with open ('StudentRecord1.dat','rb') as Myfile:
       print("\n-------DISPALY STUDENTS DETAILS--------")
       print("\nRoll No.",' ','Name','\t',end='')
       print()

       while True:
          try:
              rec=pickle.load(Myfile)
              print(' ',rec['SROLL'],'\t  ' ,rec['SNAME'])
          except EOFError:
               break

def Input():
   n=int(input("How many records you want to create :"))
   for ctr in range(n):
       sroll=int(input("Enter Roll No: "))
       sname=input("Enter Name: ")
       Writerecord(sroll,sname)

       

def SearchRecord(roll):
   with open ('StudentRecord1.dat','rb') as Myfile:
      while True:
         try:
             rec=pickle.load(Myfile)
             if rec['SROLL']==roll:
                 print("Roll NO:",rec['SROLL'])
                 print("Name:",rec['SNAME'])
         except EOFError:
             print("Record not find..............")
             print("Try Again..............")
             break

print('\nYour Choices are: ')
print('1.Insert Records')
print('2.Dispaly Records')
print('3.Search Records (By Roll No)')
print('0.Exit (Enter 0 to exit)')
ch=int(input('Enter Your Choice: '))
if ch==1: 
    Input()
elif ch==2: 
    Readrecord()
elif ch==3:
    r=int(input("Enter a Rollno to be Search: "))   
    SearchRecord(r)

print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><<><><><><><><><>")  

#question5                
import pickle
def writerecord():
      f=open("StudentDetails.dat",'wb')
      while True:
            r=int(input("Enter roll num:"))
            n=input("Enter name:")
            m=int(input("Enter marks:")) 
            rec=[r,n,m]
            pickle.dump(rec,f)  
            ch=input("Do you want to enter more records (Y/N)")
            if ch in "Nn":
                  break 
      f.close()
def read():
      f=open("StudentDetails.dat",'rb')
      try:
            while True:
                  rec=pickle.load(f)
                  print(rec)
      except EOFError:
            f.close()     

def update():
      f=open("StudentDetails.dat",'rb+')
      rollnum=int(input("Enter rollmum whose marks you want to update:"))
      try:
            while True:
                  pos=f.tell()
                  rec2=pickle.load(f)
                  if rec2[0] == rollnum:
                        um=int(input("Enter updated marks:"))
                        rec2[2]=um
                        f.seek(pos)
                        pickle.dump(rec2,f)
                  #print(rec2)
      except EOFError:
            f.close()                   

writerecord()
read()
update()
read()            
      
#question6                        
import random
def rolladice():
    counter = 0
    myList = []
    while (counter) < 6:
        randomNumber = random.randint(1,6)
        myList.append(randomNumber)
        counter = counter + 1
        if (counter)>=6:
            pass
        else:
            return myList
# Take user input here
n=1
while(n==1):
    n = int(input("Enter 1 to roll a dice and get a random number:"))
    print(rolladice())

#question7
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.head = None
 
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
 
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
 
a_stack = Stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break

#question8
import csv
with open("user_info.csv", "w") as obj:
    fileobj = csv.writer(obj)
    fileobj.writerow(["User Id", "password"])
    while(True):
        user_id = input("enter id: ")
        password = input("enter password: ")
        record = [user_id, password]
        fileobj.writerow(record)
        x = input("press Y/y to continue and N/n to terminate the program\n")
        if x in "Nn":
            break
        elif x in "Yy":
            continue
with open("user_info.csv", "r") as obj2:
    fileobj2 = csv.reader(obj2)
    given = input("enter the user id to be searched\n")
    for i in fileobj2:
        next(fileobj2)
        # print(i,given)
        if i[0] == given:
            print(i[1])
            break


