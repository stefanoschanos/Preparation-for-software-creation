from Days import Days
from Shift import Shift
from Nursing_Staff import Nursing_Staff

class Parametres(Days , Shift , Nursing_Staff):
    def __init__(self, Name , Type):
        super().__init__(Name)
        super().__init__(Type)
        super().__init__(Name)

    def Available(self):
        return 0
