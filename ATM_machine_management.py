Username="Divya"
Password="Password123"
c_name=input("Enter Your Name: ")
c_pass=str(input("Enter Your Password: "))
if c_name==Username and c_pass==Password:
    print("""
        1.Deposite
        2.Withdraw
        3.mini_statement
        4.Exit
        """)
    amount=5000
    option=int(input("Select Your Option: "))
    if option==1:
        dep=int(input("Enter The Amount: "))
        amount+=dep
        print("Total Amount : ",amount)
    elif option==2:
        withd=int(input("Enter The Amount: "))
        amount-=withd
        print("Total Amount : ",amount)
    elif option==3:
        print("*************ATM***************")
        print("Username:",Username)
        print("Total Amount: " , amount)
        print("Thanks For Visiting")
        print('*************************************')
    elif option==4:
        exit()
else:
    print("please enter your correct credientials:")
     
    
                 

