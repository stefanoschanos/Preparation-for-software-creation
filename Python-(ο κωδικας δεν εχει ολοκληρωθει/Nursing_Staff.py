from Executive import Executive
from Unit_Manager import Unit_Manager
from Nurses import Nurses 


class Nursing_Staff(Executive , Unit_Manager , Nurses):
    
    def __init__(self):
         pass

    Name = []

    with open("Staff.txt" , "r") as file:
        lines = file.readlines()
       
        for l in lines:
                as_list = l.split("\n")
                Name.append(as_list[0])
    file.close()
    
    
    def getName(self , i):
        return self.Name[i]

    def Preferences():
        pass

    