def count_sum(num1, num2):
    """складывает два числа"""
    if num1.isdigit() is True and num2.isdigit() is True:
        return f"Сумма числел равна {int(num1) + int(num2)}"
    else:
        return "Результат не известен. Число не должно содержать буквы или символы"


def count_dif(num1, num2):
    """реализует вычитание"""
    if num1.isdigit() is True and num2.isdigit() is True:
        return f"Разность числел равна {int(num1) - int(num2)}"
    else:
        return "Результат не известен. Число не должно содержать буквы или символы"
