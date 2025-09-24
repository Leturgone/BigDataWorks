
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введено не число. Попробуйте снова.")

def calc():
    a = get_number("Введите первое число: ")
    b = get_number("Введите второе число: ")
    op = input("Введите операцию (+, -, /, //, abs, pow, **): ").strip()
    result = None
    match op:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '/':
            if b != 0:
                result = a / b
            else:
                result = "Ошибка: деление на ноль"
        case '//':
            if b != 0:
                result = a // b
            else:
                result = "Ошибка: деление на ноль"
        case 'abs':
            result = (abs(a), abs(b))
        case 'pow':
            result = a ** b
        case '**':
            result = a ** b
        case _:
            result = "Неизвестная операция"
    return result

result = calc()
print(result)