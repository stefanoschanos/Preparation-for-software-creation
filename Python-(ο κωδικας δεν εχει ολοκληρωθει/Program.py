from Days import Days
from Nursing_Staff import Nursing_Staff
from Executive import Executive
from Parameters import Parametres
from Shift import Shift
from Unit_Manager import Unit_Manager
from Menu import Menu

import random

class Program(Parametres):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    d1 = Days("Monday")
    d2 = Days("Tuesday")
    d3 = Days("Wednesday")
    d4 = Days("Thursday")
    d5 = Days("Friday")
    d6 = Days("Saturday")
    d7 = Days("Sunday")

    s1 = Shift("Morning")
    s2 = Shift("Afternoon")
    s3 = Shift("Night")

    n = Nursing_Staff()
    n1 = n.getName(0)
    n2 = n.getName(1)
    n3 = n.getName(2)
    n4 = n.getName(3)
    n5 = n.getName(4)
    n6 = n.getName(5)
    n7 = n.getName(6)
    n8 = n.getName(7)
    n9 = n.getName(8)
    n10 = n.getName(9)
    n11 = n.getName(10)
    n12 = n.getName(11)
    n13 = n.getName(12)
    n14 = n.getName(13)
    n15 = n.getName(14)
    n16 = n.getName(15)
    n17 = n.getName(16)
    n18 = n.getName(17)
    n19 = n.getName(18)
    n20 = n.getName(19)
    n21 = n.getName(20)
    n22 = n.getName(21)
    n23 = n.getName(22)
    n24 = n.getName(23)

    
    E = Executive()
    U = Unit_Manager()

    """
    Staff = [n1 , n2] #, n3 , n4 , n5 , n6 , n7 , n8 , n9 , n10 , n11 , n12 , n13 , n14 , n15 , n16 , n17 , n18 , n19 , n20 , n21 , n22 , n23 ,n24]
    x = random.choice(Staff)
    print(x)
    print(Staff)
    Staff.remove(x)
    print(Staff)
    """
    print("Welcome , please choose what would you like to do")
    while (1>0):

        print("[1] Log IN , [2] Log Out , [3] Create Program , [4] Older Programs")
        Answer = input()

        if(Answer == "1"):
            print("Enter your Username")
            Username = input()
            print("Enter your Password")
            Password = input()
            Menu.Login(Username , Password)
        elif(Answer == "2"):
            Menu.Logout()
            break
        elif(Answer == "3"):

            Staff = [n1 , n2 , n3 , n4 , n5 , n6 , n7 , n8 , n9 , n10 , n11 , n12 , n13 , n14 , n15 , n16 , n17 , n18 , n19 , n20 , n21 , n22 , n23 ,n24]

            w, h = 8, 16
            Matrix = [[0 for x in range(w)] for y in range(h)]
            Matrix [0][0] = "- \t\t"
            Matrix [0][1] = "Monday"
            Matrix [0][2] = "Tuesday"
            Matrix [0][3] = "Wednesday"
            Matrix [0][4] = "Thursday" 
            Matrix [0][5] = "Friday"
            Matrix [0][6] = "Saturday"
            Matrix [0][7] = "Sunday"

            Matrix [1][0] = "\nMoring Shift\t"
            Matrix [2][0] = "- \t\t"
            Matrix [3][0] = "- \t\t"
            Matrix [4][0] = "- \t\t"
            Matrix [5][0] = "- \t\t"
            Matrix [6][0] = "- \t\t"
            Matrix [7][0] = "- \t\t"
            Matrix [8][0] = "\nAfternoon Shift "
            Matrix [9][0] = "- \t\t"
            Matrix [10][0] = "- \t\t"
            Matrix [11][0] = "- \t\t"
            Matrix [12][0] = "\nNight Shift\t"
            Matrix [13][0] = "- \t\t"
            Matrix [14][0] = "- \t\t"
            Matrix [15][0] = "- \t\t"

            Matrix [1][1] = random.choice(Staff)
            Staff.remove(Matrix[1][1])
            Matrix [2][1] = random.choice(Staff)
            Staff.remove(Matrix[2][1])
            Matrix [3][1] = random.choice(Staff)
            Staff.remove(Matrix[3][1])
            Matrix [4][1] = random.choice(Staff)
            Staff.remove(Matrix[4][1])
            Matrix [5][1] = random.choice(Staff)
            Staff.remove(Matrix[5][1])
            Matrix [6][1] = random.choice(Staff)
            Staff.remove(Matrix[6][1])
            Matrix [7][1] = random.choice(Staff)
            Staff.remove(Matrix[7][1])
            Matrix [8][1] = random.choice(Staff)
            Staff.remove(Matrix[8][1])
            Matrix [9][1] = random.choice(Staff)
            Staff.remove(Matrix[9][1])
            Matrix [10][1] = random.choice(Staff)
            Staff.remove(Matrix[10][1])
            Matrix [11][1] = random.choice(Staff)
            Staff.remove(Matrix[11][1])
            Matrix [12][1] = random.choice(Staff)
            Staff.remove(Matrix[12][1])
            Matrix [13][1] = random.choice(Staff)
            Staff.remove(Matrix[13][1])
            Matrix [14][1] = random.choice(Staff)
            Staff.remove(Matrix[14][1])
            Matrix [15][1] = random.choice(Staff)
            Staff.remove(Matrix[15][1])
            Staff = [n1 , n2 , n3 , n4 , n5 , n6 , n7 , n8 , n9 , n10 , n11 , n12 , n13 , n14 , n15 , n16 , n17 , n18 , n19 , n20 , n21 , n22 , n23 ,n24]
            
            Matrix [1][2] = random.choice(Staff)
            Staff.remove(Matrix[1][2])
            Matrix [2][2] = random.choice(Staff)
            Staff.remove(Matrix[2][2])
            Matrix [3][2] = random.choice(Staff)
            Staff.remove(Matrix[3][2])
            Matrix [4][2] = random.choice(Staff)
            Staff.remove(Matrix[4][2])
            Matrix [5][2] = random.choice(Staff)
            Staff.remove(Matrix[5][2])
            Matrix [6][2] = random.choice(Staff)
            Staff.remove(Matrix[6][2])
            Matrix [7][2] = random.choice(Staff)
            Staff.remove(Matrix[7][2])
            Matrix [8][2] = random.choice(Staff)
            Staff.remove(Matrix[8][2])
            Matrix [9][2] = random.choice(Staff)
            Staff.remove(Matrix[9][2])
            Matrix [10][2] = random.choice(Staff)
            Staff.remove(Matrix[10][2])
            Matrix [11][2] = random.choice(Staff)
            Staff.remove(Matrix[11][2])
            Matrix [12][2] = random.choice(Staff)
            Staff.remove(Matrix[12][2])
            Matrix [13][2] = random.choice(Staff)
            Staff.remove(Matrix[13][2])
            Matrix [14][2] = random.choice(Staff)
            Staff.remove(Matrix[14][2])
            Matrix [15][2] = random.choice(Staff)
            Staff.remove(Matrix[15][2])
            Staff = [n1 , n2 , n3 , n4 , n5 , n6 , n7 , n8 , n9 , n10 , n11 , n12 , n13 , n14 , n15 , n16 , n17 , n18 , n19 , n20 , n21 , n22 , n23 ,n24]

            Matrix [1][3] = random.choice(Staff)
            Staff.remove(Matrix[1][3])
            Matrix [2][3] = random.choice(Staff)
            Staff.remove(Matrix[2][3])
            Matrix [3][3] = random.choice(Staff)
            Staff.remove(Matrix[3][3])
            Matrix [4][3] = random.choice(Staff)
            Staff.remove(Matrix[4][3])
            Matrix [5][3] = random.choice(Staff)
            Staff.remove(Matrix[5][3])
            Matrix [6][3] = random.choice(Staff)
            Staff.remove(Matrix[6][3])
            Matrix [7][3] = random.choice(Staff)
            Staff.remove(Matrix[7][3])
            Matrix [8][3] = random.choice(Staff)
            Staff.remove(Matrix[8][3])
            Matrix [9][3] = random.choice(Staff)
            Staff.remove(Matrix[9][3])
            Matrix [10][3] = random.choice(Staff)
            Staff.remove(Matrix[10][3])
            Matrix [11][3] = random.choice(Staff)
            Staff.remove(Matrix[11][3])
            Matrix [12][3] = random.choice(Staff)
            Staff.remove(Matrix[12][3])
            Matrix [13][3] = random.choice(Staff)
            Staff.remove(Matrix[13][3])
            Matrix [14][3] = random.choice(Staff)
            Staff.remove(Matrix[14][3])
            Matrix [15][3] = random.choice(Staff)
            Staff.remove(Matrix[15][3])
            Staff = [n1 , n2 , n3 , n4 , n5 , n6 , n7 , n8 , n9 , n10 , n11 , n12 , n13 , n14 , n15 , n16 , n17 , n18 , n19 , n20 , n21 , n22 , n23 ,n24]

            Matrix [1][4] = random.choice(Staff)
            Staff.remove(Matrix[1][4])
            Matrix [2][4] = random.choice(Staff)
            Staff.remove(Matrix[2][4])
            Matrix [3][4] = random.choice(Staff)
            Staff.remove(Matrix[3][4])
            Matrix [4][4] = random.choice(Staff)
            Staff.remove(Matrix[4][4])
            Matrix [5][4] = random.choice(Staff)
            Staff.remove(Matrix[5][4])
            Matrix [6][4] = random.choice(Staff)
            Staff.remove(Matrix[6][4])
            Matrix [7][4] = random.choice(Staff)
            Staff.remove(Matrix[7][4])
            Matrix [8][4] = random.choice(Staff)
            Staff.remove(Matrix[8][4])
            Matrix [9][4] = random.choice(Staff)
            Staff.remove(Matrix[9][4])
            Matrix [10][4] = random.choice(Staff)
            Staff.remove(Matrix[10][4])
            Matrix [11][4] = random.choice(Staff)
            Staff.remove(Matrix[11][4])
            Matrix [12][4] = random.choice(Staff)
            Staff.remove(Matrix[12][4])
            Matrix [13][4] = random.choice(Staff)
            Staff.remove(Matrix[13][4])
            Matrix [14][4] = random.choice(Staff)
            Staff.remove(Matrix[14][4])
            Matrix [15][4] = random.choice(Staff)
            Staff.remove(Matrix[15][4])
            Staff = [n1 , n2 , n3 , n4 , n5 , n6 , n7 , n8 , n9 , n10 , n11 , n12 , n13 , n14 , n15 , n16 , n17 , n18 , n19 , n20 , n21 , n22 , n23 ,n24]

            Matrix [1][5] = random.choice(Staff)
            Staff.remove(Matrix[1][5])
            Matrix [2][5] = random.choice(Staff)
            Staff.remove(Matrix[2][5])
            Matrix [3][5] = random.choice(Staff)
            Staff.remove(Matrix[3][5])
            Matrix [4][5] = random.choice(Staff)
            Staff.remove(Matrix[4][5])
            Matrix [5][5] = random.choice(Staff)
            Staff.remove(Matrix[5][5])
            Matrix [6][5] = random.choice(Staff)
            Staff.remove(Matrix[6][5])
            Matrix [7][5] = random.choice(Staff)
            Staff.remove(Matrix[7][5])
            Matrix [8][5] = random.choice(Staff)
            Staff.remove(Matrix[8][5])
            Matrix [9][5] = random.choice(Staff)
            Staff.remove(Matrix[9][5])
            Matrix [10][5] = random.choice(Staff)
            Staff.remove(Matrix[10][5])
            Matrix [11][5] = random.choice(Staff)
            Staff.remove(Matrix[11][5])
            Matrix [12][5] = random.choice(Staff)
            Staff.remove(Matrix[12][5])
            Matrix [13][5] = random.choice(Staff)
            Staff.remove(Matrix[13][5])
            Matrix [14][5] = random.choice(Staff)
            Staff.remove(Matrix[14][5])
            Matrix [15][5] = random.choice(Staff)
            Staff.remove(Matrix[15][5])
            Staff = [n1 , n2 , n3 , n4 , n5 , n6 , n7 , n8 , n9 , n10 , n11 , n12 , n13 , n14 , n15 , n16 , n17 , n18 , n19 , n20 , n21 , n22 , n23 ,n24]

            Matrix [1][6] = random.choice(Staff)
            Staff.remove(Matrix[1][6])
            Matrix [2][6] = random.choice(Staff)
            Staff.remove(Matrix[2][6])
            Matrix [3][6] = random.choice(Staff)
            Staff.remove(Matrix[3][6])
            Matrix [4][6] = random.choice(Staff)
            Staff.remove(Matrix[4][6])
            Matrix [5][6] = random.choice(Staff)
            Staff.remove(Matrix[5][6])
            Matrix [6][6] = random.choice(Staff)
            Staff.remove(Matrix[6][6])
            Matrix [7][6] = random.choice(Staff)
            Staff.remove(Matrix[7][6])
            Matrix [8][6] = random.choice(Staff)
            Staff.remove(Matrix[8][6])
            Matrix [9][6] = random.choice(Staff)
            Staff.remove(Matrix[9][6])
            Matrix [10][6] = random.choice(Staff)
            Staff.remove(Matrix[10][6])
            Matrix [11][6] = random.choice(Staff)
            Staff.remove(Matrix[11][6])
            Matrix [12][6] = random.choice(Staff)
            Staff.remove(Matrix[12][6])
            Matrix [13][6] = random.choice(Staff)
            Staff.remove(Matrix[13][6])
            Matrix [14][6] = random.choice(Staff)
            Staff.remove(Matrix[14][6])
            Matrix [15][6] = random.choice(Staff)
            Staff.remove(Matrix[15][6])
            Staff = [n1 , n2 , n3 , n4 , n5 , n6 , n7 , n8 , n9 , n10 , n11 , n12 , n13 , n14 , n15 , n16 , n17 , n18 , n19 , n20 , n21 , n22 , n23 ,n24]

            Matrix [1][7] = random.choice(Staff)
            Staff.remove(Matrix[1][7])
            Matrix [2][7] = random.choice(Staff)
            Staff.remove(Matrix[2][7])
            Matrix [3][7] = random.choice(Staff)
            Staff.remove(Matrix[3][7])
            Matrix [4][7] = random.choice(Staff)
            Staff.remove(Matrix[4][7])
            Matrix [5][7] = random.choice(Staff)
            Staff.remove(Matrix[5][7])
            Matrix [6][7] = random.choice(Staff)
            Staff.remove(Matrix[6][7])
            Matrix [7][7] = random.choice(Staff)
            Staff.remove(Matrix[7][7])
            Matrix [8][7] = random.choice(Staff)
            Staff.remove(Matrix[8][7])
            Matrix [9][7] = random.choice(Staff)
            Staff.remove(Matrix[9][7])
            Matrix [10][7] = random.choice(Staff)
            Staff.remove(Matrix[10][7])
            Matrix [11][7] = random.choice(Staff)
            Staff.remove(Matrix[11][7])
            Matrix [12][7] = random.choice(Staff)
            Staff.remove(Matrix[12][7])
            Matrix [13][7] = random.choice(Staff)
            Staff.remove(Matrix[13][7])
            Matrix [14][7] = random.choice(Staff)
            Staff.remove(Matrix[14][7])
            Matrix [15][7] = random.choice(Staff)
            Staff.remove(Matrix[15][7])
            Staff = [n1 , n2 , n3 , n4 , n5 , n6 , n7 , n8 , n9 , n10 , n11 , n12 , n13 , n14 , n15 , n16 , n17 , n18 , n19 , n20 , n21 , n22 , n23 ,n24]
           
            for i in Matrix:
                for j in i:
                    print(j , end=" | ")
                print(sep='|') 

        elif(Answer == "4"):
            print("We are currently creating this feature , please wait for a future update")
        else:
            print("No such choice , try again")