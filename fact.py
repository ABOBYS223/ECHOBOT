def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

try:
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))

    if length <= 0 or width <= 0:
        raise ValueError("Длина и ширина должны быть положительными числами.")

    area = calculate_rectangle_area(length, width)
    perimeter = calculate_rectangle_perimeter(length, width)

    print(f"Площадь прямоугольника: {area} см")
    print(f"Периметр прямоугольника: {perimeter} см")

except ValueError as ve:
    print(f"Ошибка ввода данных: {ve}")

except Exception as e:
    print(f"Произошла ошибка: {e}")
