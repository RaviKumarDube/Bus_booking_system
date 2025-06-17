
#here is bus booking system code
# Bus Booking System
class BusBookingSystem:
    def bus_booking(self):
        bus_seat = [2,1,4,7,9,3,12,10,11]
        print("Welcome to the Bus Booking System")
        print("Available seats:", bus_seat)
        booking_seats=int(input("enter the number of seats you want to book(or type 'exit'= 0 to finish):"))
        store_seat=[]
        while booking_seats!= '0':
            for i in range(booking_seats):
              seat_number=int(input("Enter the seat number you want to book: "))
              if seat_number in bus_seat:
               store_seat.append(seat_number) 
            print("Your booked seats are:", store_seat)  
            print("congratulations! Your seats have been booked successfully.")
            exit("Thank you for using the Bus Booking System!") 


object=BusBookingSystem()
object.bus_booking()       