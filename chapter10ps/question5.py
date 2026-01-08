#  Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways

class Train:

    name = None
    age = None
    gender = None
    berth_choice = None

    No_seats = 5
    avilable_seats = 5

    def book_ticket(self, name, age, gender, berth_choice):
        self.name = name
        self.age = age
        self.gender = gender
        self.berth_choice = berth_choice

        print(f"The info is collected, if the seats is avilable you will get a 'seat confirmed message' ")
            
    
    def get_status(self, avilable_seats):
        if self.avilable_seats != 0:
            print("Your seat is confirmed!")
            print(f"Name: {self.name} \n Age: {self.age}")
        self.avilable_seats -= 1

    @staticmethod
    def fare_info():
        print("Welcome in Indian Railways!")
        print('''Ticket price is 150rs for delhi to haldwani
        Ticket price is 250rs for delhi to dehradun
        Ticket price is 1150rs for delhi to mumbai
        ''')

passanger = Train()

passanger.fare_info()
passanger.book_ticket("Deepak", 20, "M", "U")
passanger.get_status(passanger.avilable_seats)