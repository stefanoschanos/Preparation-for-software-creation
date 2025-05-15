from ast import Break


class Menu:

    def Login(name , password):
        if name == "Malcolm" and password == "M1234" or name == "Nick" and password == "N1234":
            print("Your credentials are correct")
        else:
            print("Your credentials are wrong")

    def Logout():
        print("Bye Bye")
