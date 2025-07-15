path_to_file = 'src/hangman-game/ru_nouns.txt'
game_description = '''
"Висельник" — это словесная игра, в которой один игрок загадывает слово, а другой пытается его угадать, предлагая буквы.

Правила:
    Программа выбирает слово и обозначает количество букв черточками.
    Угадывающий предлагает буквы. Если буква есть в слове, она открывается; если нет — добавляется часть тела к висельнику.
    Цель — угадать слово до завершения рисунка висельника (обычно 6-7 частей тела).
'''

def get_nouns_from_file(filename: str) -> list[str]:
    with open(filename, mode='r', encoding='utf-8') as file:
        return [noun.strip() for noun in file]
    

def print_welcome_message() -> None:
    print('Добро пожаловать в игру "Висельник"')


def print_menu() -> None:
    print('''
           ---Главное меню---
    1 - Ознакомиться с описанием игры
    2 - Начать игру
    3 - Завершить программу
    ''')


def is_contains(set_of_words: set[str], letter: str) -> bool:
    return letter in set_of_words


def print_game_description() -> None:
    print(game_description)