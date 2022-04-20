class Employees:
    def __init__(self,path):
        self.path = path
        
    def add(self):
        with open(self.path,'a') as f:
            ID = input("Enter the ID : ")
            f.write("*ID is :" + ID +"\n")
            
            Name = input("Enter the Name : ")
            f.write("*Name is :" + Name +"\n")
            
            Age = input("Enter the age : ")
            f.write("*Age is :" +Age +"\n")
            
            Sex = input("Enter the Sex : ")
            f.write("*Sex is :" +Sex +"\n")
            
            Height = input("Enter the Height : ")
            f.write("*Height is :" +Height +"\n")
            
            Weight = input("Enter the Weight : ")
            f.write("*Weight is :" +Weight +"\n")
            
            Birthday = input("Enter the Date of Birth : ")
            f.write("*Date of birth is :" + Birthday +"\n")

            f.write("\n")
            print("Employee Added!")
            
    def print(self,value):
        try:
            with open(self.path,'r') as file:
                list1 = file.readlines()
                
                value = "*ID is :" + value +"\n"
                a = list1.index(value)

                print("*"*15 + " Employee info " + "*"*15)
                print(list1[a+7])

                for i in range(a,a+7):
                    print(list1[i],end="")
                print()
                print("*"*20 + " end " + "*"*20)

        except:
            print("The entered ID is not present in the Logs")


    def delete(self,value):
        try:
            with open(self.path,'r')as f:
                list2 = f.readlines()

                value = "*ID is :" + value +"\n"
                a = list2.index(value)
            
                for i in range(0,8):
                    del list2[a]

            with open(self.path,'w') as f:
                f.writelines(list2)

            print("Employee Deleted Successfully!")
            
        except:
            print("The entered ID is not present in the Logs")

           
    def new_manager(self):
        with open(self.path,'a') as f:
            ID = input("Enter the ID : ")
            f.write("*ID is :" + ID +"\n")

            Name = input("Enter the Name : ")
            f.write("*Name is :" + Name +"\n")

            Age = input("Enter the age : ")
            f.write("*Age is :" +Age +"\n")

            Sex = input("Enter the Sex : ")
            f.write("*Sex is :" +Sex +"\n")

            Height = input("Enter the Height : ")
            f.write("*Height is :" +Height +"\n")

            Weight = input("Enter the Weight : ")
            f.write("*Weight is :" +Weight +"\n")

            Birthday = input("Enter the Date of Birth : ")
            f.write("*Date of birth is :" + Birthday +"\n")

            Department = input("Enter the Department : ")
            f.write("*Department is :" + Department +"\n")

            f.write("\n")
            print("Manager Added!")

        
Path = "log.txt"
e=Employees(Path)
import os
print("you are saving logs in : ", os.getcwd())
print("\n Welcome to employee program By Dixant Dutt ©2021 \n")

while True:
    print("""[1] Add New Employee
[2] Print Employee
[3] Delete Employee
[4] Add New Manager
[5] Exit""")
    
    choice = int(input("Enter what you want to do : "))
    if choice == 1:
        e.add()
        
    elif choice == 2:
        value=input("Enter ID : ")
        e.print(value)
        
    elif choice == 3:
        value=input("Enter ID : ")
        e.delete(value)
        
    elif choice == 4:
        e.new_manager()
        
    elif choice == 5:
        break
    else:
        print("Invalid command")
print("Program closed")
