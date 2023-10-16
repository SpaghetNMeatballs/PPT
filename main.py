def task1(im: int = 10, re: int = 5):
    print(f're = {re}, im = {im}')
    print(f'im + re = {float(im + re)}')
    print(f'im - re = {float(im - re)}')
    print(f'im * re = {float(im * re)}')
    print(f'im % re = {float(im % re)}')
    print(f'im // re = {float(im // re)}')
    print(f're + j * im = {complex(re, im)}')


def task2(length: int = 15):
    string_list = [
        " i like pizza ",
        " hot summer",
        "i often watch serials ",
        " happy new 2018 year! ",
    ]
    for s in string_list:
        print(f's.lower = {s.lower()}')
        print(f's.upper = {s.upper()}')
        print(f's capitalized = {s.rstrip().capitalize()}')
        print(f's without right chars = {s.rstrip()}')
        print(f's without left chars = {s.lstrip()}')
        print(f's filled to {length} symbols on the right = {s.rjust(length)}')
        print(f's filled to {length} symbols on the left = {s.ljust(length)}')


def task3(inp: str = 'Революция!'):
    return inp[:4] + inp[-4:]


def task4(inp: int = 12):
    print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(inp))
    print(f"bin: {inp: b}, oct: {inp: o}, hex: {inp: x}")


def main() -> None:
    print('\tЗадание 1')
    task1()
    print('\tЗадание 2')
    task2()
    print('\tЗадание 3')
    # Здесь ставим принт потому что таск3 возвращает результат слайса в виде строки
    print(task3())
    print('\tЗадание 4')
    task4()


if __name__ == '__main__':
    main()
