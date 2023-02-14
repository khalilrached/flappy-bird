import unittest

from lib import Pilar


class MyTestCase(unittest.TestCase):
    def test_something(self):
        i = 0
        while i < 1000 :
            pilar = Pilar(100, 100)
            print(f"gap_distance: {pilar.gap_height}, gap_position: {pilar.gap_y_center}")
            self.assertLess(pilar.gap_y_center,100,"greater than 100")  # add assertion here
            self.assertGreater(pilar.gap_y_center,0,"less than 0")  # add assertion here
            i += 1


if __name__ == '__main__':
    unittest.main()
