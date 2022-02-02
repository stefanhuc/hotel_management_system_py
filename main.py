class hotelmanage:

    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=125, name='', address='', cindate='', coutdate='', rno=1, total = 0):

        print("\n\n*****WELCOME TO Buena Vista Hotel *****\n")

        self.rt = rt

        self.r = r

        self.t = t

        self.p = p

        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno
        self.total = 0

    def inputdata(self):
        self.name = input("\nEnter your full name:")
        self.address = input("\nEnter your address:")
        self.cindate = input("\nEnter your check in date:")
        self.coutdate = input("\nEnter your check out date:")
        print("Your room no.:", self.rno, "\n")

    def roomrent(self):

        print("We have the following rooms for you:-")

        print("1.  Class A---->1500")

        print("2.  Class B---->700")

        print("3.  Class C---->200")

        print("4.  Class D---->100")

        x = int(input("Enter the number of your choice:->"))

        n = int(input("For how many nights did you stay:"))

        if (x == 1):

            print("You have choose room Class A")

            self.s = 1500 * n

        elif (x == 2):

            print("You have choose room Class B")

            self.s = 700 * n

        elif (x == 3):

            print("You have choose room Class C")

            self.s = 200 * n

        elif (x == 4):
            print("You have choose room Class D")

            self.s = 100 * n

        else:

            print("please choose a room")

        print("Your chosen room rent is: ${0}".format(self.s), "\n")

    def foodpurchased(self):

        print("*****Restaurant Menu*****")

        print("1.Dessert----->15", "2.Drinks----->7", "3.Breakfast---   >9", "4.Lunch---->11", "5.Dinner--->15",
              "6.Exit")

        while (1):

            c = int(input("Enter the number of your choice: "))

            if (c == 1):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 15 * d

            elif (c == 2):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 5 * d

            elif (c == 3):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 9 * d

            elif (c == 4):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 11 * d

            elif (c == 5):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 15 * d

            elif (c == 6):
                break;
            else:
                print("You've Enter an Invalid Key")

        print("Total food cost: ${0}".format(self.r), "\n")

    def display(self):
        print("******The bills******")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check in date:", self.cindate)
        print("Check out date", self.coutdate)
        print("Room no.", self.rno)
        print("Your Room rent is:", self.s)
        print("Your Food bill is:", self.r)

        self.rt = self.s + self.t + self.p + self.r

        print("Your sub total purchased is: ${0}".format(self.rt))
        print("Additional service charges is: ${0}".format(self.a))
        self.total = self.rt + self.a
        print("Your grand total purchased is: ${0}".format(self.total), "\n")
        self.rno += 1


def main():
    a = hotelmanage()

    while (1):
        print("1.Enter Customer Data")

        print("2.Calculate Room Rent")

        print("3.Calculate Food Purchased")

        print("4.Show total cost")

        print("5.EXIT")

        b = int(input("\nEnter the number of your choice:"))
        if (b == 1):
            a.inputdata()

        if (b == 2):
            a.roomrent()

        if (b == 3):
            a.foodpurchased()

        if (b == 4):
            a.display()

        if (b == 5):
            quit()


main()