import random
password=[]
randlett=0
randnum=0
spcharchoice=0
letterlist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
spcharlist=["!","@","#","$","%","^","&","*","(",")","-","_","=","+",",","<",".",">",";",":"]

    
while True:
    num=input("Enter number of integers:")
    if num.isnumeric():
        num=int(num)
        break
    else:
        print("Invalid")
        continue
while True:
    lett=input("Enter number of letters:")
    if lett.isnumeric():
        lett=int(lett)
        break
    else:
        print("Invalid")
        continue
while True:
    spchar=input("Enter number of special characters:")
    if spchar.isnumeric():
        spchar=int(spchar)
        break
    else:
        print("Invalid")
        continue


total=int(spchar)+int(lett)+int(num)

while total>0:
    total=spchar+lett+num
    choice=random.randint(1,3)

    if choice==1 and lett>0:
        randlett=random.choice(letterlist)
        lett=lett-1
        password.append(randlett)

    if choice==2 and num>0:
        randnum=random.randint(0,9)
        num=num-1
        randnum=str(randnum)
        password.append(randnum)

    if choice==3 and spchar>0:
        spcharchoice=random.choice(spcharlist)
        spchar=spchar-1
        password.append(spcharchoice)

#output        
random.shuffle(password)
print("".join(password))