def bus_seat():
    bus_seat = [2, 1, 4, 7, 9, 3, 12, 10, 11]
    print("Welcome to the Bus Booking System")
    print("Available seats:", bus_seat)
    booking_seats = int(input("Enter the number of seats you want to book (or type '0' to finish): "))
    store_seat = []
    
    while booking_seats != 0:
        for i in range(booking_seats):
            seat_number = int(input("Enter the seat number you want to book: "))
            if seat_number in bus_seat:
                store_seat.append(seat_number)
                bus_seat.remove(seat_number)  # Remove booked seat from available seats
                print("Seat booked successfully!")
            else:
                print("Seat number not available. Please choose another seat.")
        
        print("Booked seats:", store_seat)
        booking_seats = int(input("Enter the number of seats you want to book (or type '0' to finish): "))
    
    print("Thank you for using the Bus Booking System!")

bus_seat()
