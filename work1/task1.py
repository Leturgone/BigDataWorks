import math
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введено не число. Попробуйте снова.")

def calculate_area():
    areas = {}
    
    fig = input("Введите фигуру (треугольник, прямоугольник, круг): ").strip().lower()
    match fig:
        case 'треугольник':
            l = get_number("Введите длину основания: ")
            h = get_number("Введите высоту: ")
            area = 0.5 * l * h
            areas['треугольник'] = area
        case 'прямоугольник':
            w = get_number("Введите ширину: ")
            h = get_number("Введите высоту: ")
            area = w * h
            areas['прямоугольник'] = area
        case 'круг':
            r = get_number("Введите радиус: ")
            area = math.pi * r ** 2
            areas['круг'] = area
        case _:
            print("На вход приимаются только треугольник, прямоугольник, круг ")
                    
    return areas

result = calculate_area()
print(result)