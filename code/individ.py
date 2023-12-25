def sum_decorator(start):
    def decorator(func):
        def wrapper(numbers_str):
            numbers = list(map(int, numbers_str.split()))
            result = func(numbers)
            return result + start

        return wrapper

    return decorator

@sum_decorator(start=5)
def calculate_sum(numbers):
    return sum(numbers)

if __name__ == "__main__":
    input_numbers = input("Введите строку целых чисел через пробел: ")
    result = calculate_sum(input_numbers)
    print(f"Сумма чисел с учетом декоратора: {result}")