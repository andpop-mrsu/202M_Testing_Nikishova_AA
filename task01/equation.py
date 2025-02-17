import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return None  # Уравнение не имеет решений
        return [-c / b]  # Линейное уравнение bx + c = 0
    
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant < 0:
        return None  # Уравнение не имеет действительных решений
    elif discriminant == 0:
        root = -b / (2 * a)
        return [root, root]  # Два одинаковых корня
    else:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return sorted([root1, root2])  # Два корня в порядке возрастания
    
print(solve_quadratic(1, -3, 2))