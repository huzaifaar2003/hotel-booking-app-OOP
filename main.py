import pandas as pd

# class User:
#     def view_hotels(self):
#         pass
#
#     pass
# view_hotels() method removed. Since User class has no methods the class is then removed

df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")

df = pd.read_csv("hotels.csv")

class Hotel:
    watermark = "The Hotel Booking Company"
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

    @classmethod
    def get_hotel_count(cls, dataframe):
        return len(dataframe)

    def __eq__(self,other):
        if self.id == other.id:
            return True
        else:
            return False





class SpaHotel(Hotel):
    def book_spa(self):
        # print("Hurray! Great choice! Spa confirm!!!!\n")
        pass

class Confirmation:
    def __init__(self, customer_name, Hotel_object):
        self.name = customer_name
        self.hotel = Hotel_object

    def generate(self):
        content = f"{self.the_customer_name}'s booking is confirmed at {self.hotel.name}"
        # self.the_customer_name using class property
        return content

    @property
    def the_customer_name(self):
        name = self.name.strip()
        name=name.title()
        return name

    @staticmethod
    def convert_eur_to_usd(amount_eur):
        return amount_eur*1.2


class SpaConfirmation():
    def __init__(self, customer_name, Hotel_object):
        self.name = customer_name
        self.hotel = Hotel_object
    def generate(self):
        content = f"{self.name}'s Spa booking is confirmed at {self.hotel.name}"
        return content





class CreditCard:
    def __init__(self, number):
        self.number = number
    def validate(self, expiration, holder, cvc):
        card_dict = {"number": self.number,
                     "expiration": expiration,
                     "holder": holder,
                     "cvc":cvc}
        if card_dict in df_cards:
            # checks if that exact dictionary set of values is in the "df_cards" list of dictionaries
            return True
        else:
            return False

df_auth = pd.read_csv("card_security.csv", dtype=str).to_dict(orient="records")

class SecureCreditCard(CreditCard):
    def authenticate(self, password):
        auth_dict = {"number":self.number,
                     "password": password}
        if auth_dict in df_auth:
            return True
        else:
            return False


print(df)
hotel_id = input("Enter hotel id: ")

hotel = SpaHotel(int(hotel_id)) # explicit declaration of "hotel_id"

if hotel.available():
    card_number = input("Enter card number: ") # "1234" - inputs are by default strings
    card_exp = input("Enter expiration date: MM/YY ")
    card_name = input("Enter card holder name as displayed on card\nex: ABDULLAH QASIM: ")
    card_cvc = input("Enter cvc:\nex: 123: ")
    card_password = input("Enter card password: ")
    card=SecureCreditCard(card_number)
    if card.validate(card_exp,card_name,card_cvc):
        if card.authenticate(card_password):
            hotel.book()
            name = input("Enter your name: ")
            confirmation = Confirmation(name, hotel)
            print(confirmation.generate())
            spa_input = input("\nWould you like to book a Spa package? ")
            if spa_input == "yes":
                hotel.book_spa()
                spa_confirmation = SpaConfirmation(name, hotel)
                print(f"\n{spa_confirmation.generate()}")
            else:
                print("\nThank you! Here are your details again\n")
                print(confirmation.generate())
        else:
            print("Authentication error!\n")
    else:
        print("Payment method error.\n")
else:
    print("\nHotel unavailable")



