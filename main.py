import pandas as pd

# class User:
#     def view_hotels(self):
#         pass
#
#     pass
# view_hotels() method removed. Since User class has no methods the class is then removed

class Hotel:
    def __init__(self, id):
        self.id = id
        self.name = df.loc[df["id"]==self.id, "name"].squeeze() # added this when implementing Confirmation class


    def available(self):
        availablity = df.loc[df["id"]==self.id, "available"].squeeze()
        if "yes" == availablity:
            return True
        else:
            return False


    def book(self):
        df.loc[df["id"]==self.id, "available"] = "no"
        df.to_csv("hotels.csv", index = False)
        print("Booking done.")



class Confirmation:
    def __init__(self, customer_name, Hotel_object):
        self.name = customer_name
        self.hotel = Hotel_object
    def generate(self):
        content = f"{self.name}'s booking is confirmed at {self.hotel.name}"
        return content

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



