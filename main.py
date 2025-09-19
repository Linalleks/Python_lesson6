def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def has_upper_letters(password):
    for char in password:
        if char.isupper():
            return True
    return False


def has_lower_letters(password):
    for char in password:
        if char.islower():
            return True
    return False


def has_symbols(password):
    symbols = '!@#$%^&*()_+-="№;%:?}{[]\\|/`~'
    for char in password:
        if symbols.find(char) > -1:
            return True
    return False


def main():
    password_checks = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]
    score = 0
    password = input('Введите пароль: ')

    for check in password_checks:
        if check(password):
            score += 2

    print(f'Рейтинг пароля: {score}')


if __name__ == '__main__':
    main()
