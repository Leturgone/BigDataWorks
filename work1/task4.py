def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введено не число. Попробуйте снова.")

def print_seq():
    N = get_number("Введите неотрицательное целое число N: ")
    sequence = []
    for i in range(1, N + 1):
        sequence.extend([i] * i)
    print(*sequence)

print_seq()