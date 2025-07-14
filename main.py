import pandas as pd

# class User:
#     def view_hotels(self):
#         pass
#
#     pass
# view_hotels() method removed. Since User class has no methods the class is then removed

class Hotel:
    def __init__(self, id):
        pass


    def available(self):
        pass


    def book(self):
        pass



class Confirmation:
    def __init__(self, customer_name, Hotel_object):
        pass
    def generate(self):
        pass

    pass

df = pd.read_csv("hotels.csv")
print(df)
hotel_id = input("Enter hotel id: ")

hotel = Hotel(int(hotel_id)) # explicit declaration of "hotel_id"

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    confirmation = Confirmation(name, hotel)
    print(confirmation.generate())
else:
    print("\nHotel unavailable")



