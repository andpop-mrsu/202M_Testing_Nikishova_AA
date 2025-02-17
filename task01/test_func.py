import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestGetTriangleType(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")
        self.assertEqual(get_triangle_type(10, 10, 10), "equilateral")
    
    def test_isosceles(self):
        self.assertEqual(get_triangle_type(3, 3, 4), "isosceles")
        self.assertEqual(get_triangle_type(5, 5, 8), "isosceles")
    
    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")
        self.assertEqual(get_triangle_type(7, 10, 12), "nonequilateral")
    
    def test_incor_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 0, 0)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, -1, -1)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(10, 1, 1)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 2, 2)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, -2, -4)

if __name__ == "__main__":
    unittest.main()