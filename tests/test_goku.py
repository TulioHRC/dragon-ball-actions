import unittest
from gameplay.goku import Goku


class TestGoku(unittest.TestCase):

    def test_constructor(self):
        goku = Goku(9000, 10, 20)

        self.assertEqual(goku.get_power(), 9000)
        self.assertEqual(goku.get_x(), 10)
        self.assertEqual(goku.get_y(), 20)

    def test_move_vertical_positive(self):
        goku = Goku(9000, 0, 0)

        goku.move_vertical(5)

        self.assertEqual(goku.get_y(), 5)

    def test_move_vertical_negative(self):
        goku = Goku(9000, 0, 0)

        goku.move_vertical(-3)

        self.assertEqual(goku.get_y(), -3)

    def test_move_horizontal_positive(self):
        goku = Goku(9000, 0, 0)

        goku.move_horizontal(7)

        self.assertEqual(goku.get_x(), 7)

    def test_move_horizontal_negative(self):
        goku = Goku(9000, 0, 0)

        goku.move_horizontal(-4)

        self.assertEqual(goku.get_x(), -4)

    def test_multiple_movements(self):
        goku = Goku(9000, 0, 0)

        goku.move_horizontal(3)
        goku.move_vertical(2)
        goku.move_horizontal(-1)

        self.assertEqual(goku.get_x(), 2)
        self.assertEqual(goku.get_y(), 2)


if __name__ == "__main__":
    unittest.main()