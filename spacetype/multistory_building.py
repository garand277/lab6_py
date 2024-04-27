from spacetype import Apartment

class MultistoryBuilding(Apartment):
    def __init__(self, height, width, length, num_floors, num_rooms):
        super().__init__(height, length, width, num_rooms)
        self.num_floors = num_floors

    def calculate_total_area(self):
        return super().calculate_total_area * self.num_floors
    
    def calculate_heat_power(self):
        return self.calculate_total_area * 30.2