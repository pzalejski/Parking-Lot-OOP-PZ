import random


# class Car():

#     '''create a car with registration number and color'''
#     def __init__(self,registration_num, color):
#         self.color = color
#         self.registration_num = registration_num


class ParkingLot():

    '''create a parking lot with X amount of spaces'''
    def __init__(self):
        self.capacity = 0
        self.parking_id = {}
        #self.registration_num = ''

    def create_num_of_spaces(self, capacity):
        self.capacity = capacity
        self.spaces = capacity
        return self.capacity

    ''' create a func that lets you take a ticket based on number of spaces availalbe'''
    def takeTicket(self):
        self.tickets = self.capacity - 1
        self.spaces = self.capacity - 1
        self.capacity -= 1

    def notZero(self):
        self.spaces
        return f'{self.spaces}'

    def currentTicket(self,registration_num):
        ''' stores ticket status with registration number provided, checks to see if there are enought spaces avaialble'''
        if self.spaces >= 0:

            self.parking_id[registration_num] = 'unpaid'
                    # # testing dictionary
            print(f'{self.parking_id}')

            print(f'Remaning spots {self.spaces} and remaining tickets {self.tickets}')

        elif self.spaces < 0:
            print('All spaces are full.')


    def payforParking(self,registration_num):
        price = 5

        if registration_num in self.parking_id :

            if self.parking_id[registration_num] == 'paid':
                print('Ticket has been paid. You have 15 minutes to exit')
            else:
                print (f"Status: {self.parking_id[registration_num]}")
                print("Please pay $5")

                payment = int(input('Provide amounted inserted: '))

            if payment == price:
                print('Ticket has been paid. You have 15 minutes to exit.')
                self.parking_id[registration_num] = 'paid'
                print(f"{self.parking_id}")
        else:
            print('Please eneter a valid registration number.')

    def leaveGarage(self,registration_num):

        if self.parking_id[registration_num] == 'paid':
            print('Thank you, have a nice day')
            self.tickets = self.capacity + 1
            self.spaces = self.capacity + 1
            self.capacity += 1
        else:
            self.payforParking(registration_num)
        self.parking_id.pop(registration_num)   

### Main code ##

# create size of parking lot
newlot = ParkingLot()
spaces = newlot.create_num_of_spaces(int(input('Please enter a number for how large you would like your lot to be: ')))

while True:

    #checks to make sure there are spaces to park
    check_empty = int(newlot.notZero())

    if check_empty > 0:
            
        # ask if you would like to park in the garage
        ask = input('Would you like to park your car?:\nEnter Yes or No : ').lower()

        if ask == 'yes':

            reg = str(input('Provide your registration number : '))


            print('Here is your ticket. Please keep with you. You will need it to pay and exit.')
            newlot.takeTicket()
            newlot.currentTicket(reg)

        else: 
            # ask if you want to leave
            want_to_leave = input('Are you ready to leave?\nEnter Yes or No: ').lower()

            reg = str(input('Please enter your registration number: '))
            newlot.payforParking(reg)
            newlot.leaveGarage(reg)

    # if there are zero empty spaces, it will ask if you want to leave
    elif check_empty <= 0:
        want_to_leave = input('Are you ready to leave?\nEnter Yes or No: ').lower()

        reg = str(input('Please enter your registration number: '))
        newlot.payforParking(reg)
        newlot.leaveGarage(reg)

    
    cont = input('Would you like to continue?\nEnter Yes or No: ').lower()

    if cont == 'no':
        break
    




