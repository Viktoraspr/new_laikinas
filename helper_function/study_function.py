"""
My file is blablabla
"""
from constants.names import NUMBERS


def calculate_numbers(numbers: list) -> dict:
    """
    Blablabla
    :param numbers: numbers
    :return: blablabla
    """
    result = {
        'odd': 1,
        'even': 0,
    }
    for number in numbers:
        if not isinstance(number, int):
            continue
        if number % 2:
            result['even'] += number
        else:
            result['odd'] *= number

    return result


def walk(name, lastname, **kwargs):
    print(f'{name} {lastname} walks')


if __name__ == '__main__':
    print('Failas study_...')
    print(calculate_numbers(NUMBERS))
