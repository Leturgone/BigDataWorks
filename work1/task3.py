from collections import deque

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введено не число. Попробуйте снова.")


def while_sum():
    queue = deque()
    total_sum = 0

    while True:
        try:
            num = get_number("Введите число: ")
            queue.append(num)
            total_sum += num
            if total_sum == 0:
                break
        except ValueError:
            print("Ошибка: введено не число. Попробуйте снова.")

    sum_of_squares = sum(x ** 2 for x in queue)
    print("Сумма квадратов считанных чисел:", sum_of_squares)
    
    
while_sum()