import unittest

from gameplay.goku import Goku
from gameplay.game import Game


class TestGame(unittest.TestCase):

    def test_game_starts_running(self):
        player = Goku(9000, 0, 0)
        game = Game(player, 1, 1, 10000)

        self.assertTrue(game.get_status())

    def test_player_loses_when_enemy_is_stronger_and_same_position(self):
        player = Goku(5000, 2, 3)
        game = Game(
            player=player,
            enemy_x=2,
            enemy_y=3,
            enemy_power=10000
        )

        game.battle()

        self.assertFalse(game.get_status())

    def test_player_survives_when_enemy_is_weaker(self):
        player = Goku(10000, 2, 3)
        game = Game(
            player=player,
            enemy_x=2,
            enemy_y=3,
            enemy_power=5000
        )

        game.battle()

        self.assertTrue(game.get_status())

    def test_player_survives_when_enemy_has_same_power(self):
        player = Goku(5000, 2, 3)
        game = Game(
            player=player,
            enemy_x=2,
            enemy_y=3,
            enemy_power=5000
        )

        game.battle()

        self.assertTrue(game.get_status())

    def test_player_survives_when_not_same_position(self):
        player = Goku(1000, 0, 0)
        game = Game(
            player=player,
            enemy_x=5,
            enemy_y=5,
            enemy_power=100000
        )

        game.battle()

        self.assertTrue(game.get_status())


if __name__ == "__main__":
    unittest.main()