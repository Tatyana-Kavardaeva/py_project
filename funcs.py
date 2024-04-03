def count_sum(num1, num2):
    """складывает два числа"""
    if num1.isdigit() is True and num2.isdigit() is True:
        return f"Сумма числел равна {int(num1) + int(num2)}"
    else:
        return "Результат не известен. Число не должно содержать буквы или символы"


number1 = input("Введите число")
number2 = input("На сколько Вы хотите его увеличить?")
print(count_sum(number1, number2))
