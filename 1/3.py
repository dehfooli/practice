name= str(input("please enter name: "))
family= str(input("please enter family: "))
mark1= float(input("please enter mark 1: "))
mark2= float(input("please enter mark 2: "))
mark3= float(input("please enter mark 3: "))

GPA = (mark1+mark2+mark3) / 3

if GPA >= 17:
    print("Great")
elif GPA < 17 and GPA >= 12:
    print("Normal")
else: 
    GPA < 12
    print ("Fail") 
print(GPA)