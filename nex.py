
def calculator():
    print("Простой консольный калькулятор")
    print("Доступные операции: +, -, *, /")

    while True:
        try:
            operation = input("Введите операцию (или 'выход' для выхода): ")

            if operation.lower() == 'выход':
                print("Программа завершена.")
                break

            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if operation in ('+', '-', '*', '/'):
                result = eval(f"{num1} {operation} {num2}")
                print(f"Результат: {result}")
            else:
                print("Неверная операция. Повторите ввод.")

        except ValueError:
            print("Ошибка: введите числа корректно.")
        except ZeroDivisionError:
            print("Ошибка: деление на ноль.")
        except Exception as e:
            print(f"Ошибка: {e}")
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y if y != 0 else "Ошибка: деление на ноль"


if __name__ == "__main__":
    calculator()
