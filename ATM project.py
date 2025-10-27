#build a application
#project name-ATM
while True:
    amount=100000
    password=1234
    card=input("insert the card:")
    if card=="c":
        print("Welcome Eswar")
        if password==password:
                        option=int(input('''enter the option
                                                        1.balance enquiry
                                                        2.withdraw '''))
                        if option==1:
                            print("your acount balance:",amount)
                        elif option==2:
                            money=int(input('enter the amount:'))
                            print(money)
                            balance=amount-money
                            print("remaining amount:",balance)
        else:
            print("invalid credentials")
    else:
        print("invalid card")
                                   
                    
       

