from spacetype.room import Room

class Apartment(Room):
    def __init__(self, height, lenght, width, room_num):
        super().__init__(height, lenght, width)
        self.room_num = room_num

    def calc_total_area(self):
        return self.calc_area() * self.room_num
    
    def calc_heat_power(self):
        return self.calc_total_area * 30.2