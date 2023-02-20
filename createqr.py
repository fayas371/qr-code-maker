import pyqrcode
choice = input(" choose Y/N ")
def employee_details():
#for saving and writing the file
    myfile=open("gpa.txt","w")

#for storing user details
    while True:
        condition=input("do you want to enter thd details")
        #for checking the user entered yes or no
        if condition.lower()[0] == 'y':
            employee_name=input("Enter employee name:")
            employee_age=input("Enter a employee age")
            gender=input("Enter gender")
            mobileno=int(input("Enter your mobile no"))
            salary=float(input("Enter your salary"))
            #for saving the file in employee name
            myfile=open(employee_name,"w")
            myfile.write(f"Name:{employee_name}\nAge:{employee_age}\ngender:{gender}\nmobile no:{mobileno}\nsalary:{salary}")
            #for creation for qrcode
            ss=employee_name+".svg"
            url=pyqrcode.create("Name:"+employee_name+"\n"+"Age:"+employee_age)
            url.svg(ss, scale = 8)
            print("data stored")
        else:
            break

if choice=='y':
    employee_details()
else:
    print("invalid")







