class Room:
    def __init__(self, lenght, wight, height):
        self.lenght = lenght
        self.wight = wight
        self.height = height

    def calc_area(self):
        return self.height * self.lenght * self.wight
    
    def calc_heat_power(self):
        return self.calc_area * 30,2