accountbalance = 3000
pin = 1234
accountname = "Olaoluwa Oyebola"

userpin = input("Enter your Pin >> ")
try:
    #userpin = int(userpin)
    while True:
        userpin = int(userpin)
        if userpin != pin:
            userpin = int(input("\nInvalid pin Re-enter: "))
        while True:
            if userpin == pin:
                task = input("""What do you want to do: 
                1. Withdraw
                2. Transfer
                3. Change pin
                >> """)
                if task == '1':
                    amount = int(input("Amount>> "))
                    if amount <= accountbalance - 1000:     # minus 1000 is to leave a minimum of 1000 in the account
                        print("Please take your cash")
                    else:
                        print("Insufficient funds")
                    
                elif task == '2':
                    accountnum = input("Enter recipient account number>> ")
                    bankname = input("recipient bank name>> ")
                    amount = int(input("enter amount you want to send>> "))
                    if amount <= accountbalance - 1000:
                        print("Transfer successful")
                    else:
                        print("Insufficient funds")
                
                elif task == '3':
                    userpin = input("Enter current pin>> ")
                    newpin = input("Enter new pin>> ")
                    if newpin != userpin:
                        print("You have successfully changed your pin")
                    else:
                        print("You can't make use of previous pin")
            
            else:
                print("Wrong pin, Try again")
            break
        # if userpin != pin:
        #     userpin = int(input("\nInvalid pin Re-enter: "))
        break    
except ValueError:
    print("Invalid input")

            


