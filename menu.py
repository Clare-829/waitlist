from waitlist import Waitlist
class Menu:
    """A class representing the menu for the restaurant reservation program"""

    def __init__(self):
        """Initialize the menu with the waitlist object"""
        self.waitlist = Waitlist()

    def run(self):
        """Print the main menu"""
        print("Welcome to the Restaurant Reservation System!")
        print("==============================================")
        print("Please select an option:")
        print("1. Add a customer to the waitlist")
        print("2. Seat the next customer")
        print("3. Change the time of a customer's reservation")
        print("4. Peek at the next customer")
        print("5. Print the reservation list")
        print("6. Quit")
        print("")
        while True:
            
            choice = input("Enter your choice (1-6): ")
            print("*************************************************")
            #Each one of these options should call a method from Waitlist class 
            if choice == "1":
                self.name = input('Enter name :')
                self.time = input('Enter time :')


                self.waitlist.add_customer(self.name, self.time)

                print(self.waitlist)


            elif choice == "2":
                self.waitlist.seat_customer()
                print(self.waitlist)

            elif choice == "3":
                name = input("Enter a name: ")
                hours =  input("Which new hour would you like to be at?: ")
                mins = input("Which new minute would you like to be at?: ")
                new_priority = self.waitlist.Time(hours,mins)
                self.waitlist.change_reservation(name, new_priority)

            elif choice == "4":
                self.waitlist.peek()

            elif choice == "5":
                 print(self.waitlist)
            elif choice == "6":
                """exit the program at any time"""
                print("Thank you for using the Restaurant Reservation System!")
                break
            else:
                print("Invalid choice. Try again.")
    

s = Menu()
s.run()
