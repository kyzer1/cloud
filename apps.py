from travel_agency import user_creator, trip_creator, show_user, tour_creator, show_trip, show_tour

def menu():

    print('''
    select :
    1-createuser
    2-showuser
    3-addtrip
    4-showtrip
    5-addtour
    6-showtour
    ''')

    option = int(input("enter number:"))

    if option == 1:
        name=input("name: ")
        phone_number=input("phone_number: ")
        age=input("age: ")
        user_creator(name, phone_number, age)
        

        back_to_menu = input("press anykey to return...")
        menu()

    elif option == 2:
        name = input("name: ")

        print(show_user(name))

        back_to_menu = input("press anykey to return...")
        menu()

    elif option == 3:
        start = input("from: ")
        destination = input("destination: ")
        time = input("date: ")
        vehicle = input("vehicle: ")
        users = input("travelers: ")

        trip_creator(start, destination, time, vehicle, users)


        back_to_menu = input("press anykey to return...")
        menu()

    elif option == 4:
        start = input("start: ")
        destination = input("destination: ")
        time = input("date: ")

        print(show_trip(start, destination, time))
        back_to_menu = input("press anykey to return...")
        menu()

    if option == 5:

        start = input("start: ")
        destination = input("destination: ")
        days = input("days: ")
        price = input("price: ")
        users = input("travelers: ")
        tour_leader = input("tour leader: ")
        details = input("details: ")


        tour_creator(tour_leader, users, days, price, start, destination, details)

        back_to_menu = input("press anykey to return...")
        menu()

    if option == 6:
        start = input("start: ")
        destination=input("destination: ")
        leader=input("leader: ")


        show_tour(start, destination, leader)

        back_to_menu = input("press anykey to return...")
        menu()


menu()