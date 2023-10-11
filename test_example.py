# Для интересующихся - пример юнит-тестов
# В рамках лаб может пригодится для проверки задач, у которых есть пример ввода и вывода, например, 3 задание 2 лабы
# Сначала импортируем нашу тестируемую функцию из файла, где она реализована
from example_script import some_calc_func


# Далее напишем сам юнит-тест
def test_some_calc_func():
    # Здесь через проверку assert удостоверимся, что наша функция реализует ожидаемое от неё поведение
    assert some_calc_func(5, 10) == 15

# В этом файле не нужно реализовать main функцию и проверку на исполнение
# При вызове метода pytest через консоль пайтест сам пройдёт по директории, соберёт все файлы с началом test
# И запустит все тесты вида test_*
# Для более глубокого изучения рекомендую прочитать доки https://docs.pytest.org/
