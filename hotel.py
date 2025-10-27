def hotel():
    print("\nWelcome to the Hotel")
    print("1. Room Booking")
    print("2. Food Order")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nRoom Types:")
        print("1. AC")
        print("2. Non-AC")
        room_type = int(input("Choose room type: "))

        print("\nTypes:")
        print("1. Single Room")
        print("2. Double Room")
        type = int(input("Choose type: "))

        if room_type == 1 and type == 1:
            payment=int(input("\nEnter the amount: "))
            if payment==4000:
                print(f"AC Single Room of {payment}/- is Booked")
            else:
                print(("no rooms available in your budget").title())
        elif room_type == 1 and type == 2:
            if payment==6000:
                print(f"AC Double Room of {payment}/- is Booked")
            else:
                print(("no rooms available in your budget").title())
        elif room_type == 2 and type == 1:
            if payment==750:
                print(f"Non-AC Single Room of {payment}/- is Booked")
            else:
                print(("no rooms available in your budget").title())
        elif room_type == 2 and type == 2:
            if payment==1200:
                print(f"Non-AC Double Room of {payment}/- is Booked")
            else:
                print(("no rooms are available in your budget").title())
        else:
            print("Invalid selection")

    elif choice == 2:
        food = input("Enter your food order: ")
        print(f"Your order for '{food}' has been placed!")

    else:
        print("Invalid choice!")
    hotel()
hotel()
