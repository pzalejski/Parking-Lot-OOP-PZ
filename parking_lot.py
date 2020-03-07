

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

    def create_num_of_spaces(self, capacity):
        self.capacity = capacity
        self.spaces = capacity
        return f"This parking lot has {self.capacity} spaces"

    ''' create a func that lets you take a ticket based on number of spaces availalbe'''
    def takeTicket(self):
        self.tickets = self.capacity - 1
        self.spaces = self.capacity - 1
        # testing if tickets and spaces available are reduced
        # print('You have taken a ticket')

    def currentTicket(self):
        ''' stores ticket status with registration number provided, checks to see if there are enought spaces avaialble'''
        if self.spaces >= 0:
            registration_num = input('Please provide your registration number: ')

            self.parking_id[registration_num] = 'unpaid'

            print(f'Remaning spots {self.spaces} and remaining tickets {self.tickets}')

        elif self.spaces < 0:
            print('All spaces are full.')

        # testing dictionary
        print(f'{self.parking_id}')




car1 = ParkingLot()
print(car1.create_num_of_spaces(1))
car1.takeTicket()
car1.currentTicket()
car2 = ParkingLot()
car2.takeTicket()
