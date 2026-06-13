class Game:
    def __init__(self, player: Goku, enemy_x: int, enemy_y: int, enemy_power: float):
        self.player = player
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.enemy_power = enemy_power
        self.is_running = True

    def battle(self):
        if (self.enemy_x == self.player.get_x() and self.enemy_y == self.player.get_y() and self.enemy_power > self.player.get_power()):
            self.is_running = False

        print('Sem batalhas aqui!')
    
    def get_status(self):
        return self.is_running