class Goku:
    def __init__(self, power_level: float, x: int, y: int):
        self.power_level = power_level
        self.x = x
        self.y = y

    def move_vertical(self, spaces: int):
        self.y += spaces
    
    def move_horizontal(self, spaces: int):
        self.x += spaces
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_power(self):
        return self.power_level