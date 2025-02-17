import pytest
from triangle_class import Triangle, IncorrectTriangleSides

def test_triangle_positive():
    t = Triangle(3, 3, 3)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 9

    t = Triangle(3, 3, 4)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 10

    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12

    t = Triangle(10, 10, 10)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 30

    t = Triangle(5, 5, 8)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 18
    
    t = Triangle(7, 10, 12)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 29

def test_triangle_negative():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 0, 0)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, -1, -1)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(10, 1, 1)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 2, 2)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(3, -2, -4)

print(test_triangle_positive())
print(test_triangle_negative())