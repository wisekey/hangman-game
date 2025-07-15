path_to_file = 'src/hangman-game/ru_nouns.txt'
game_description = '''
---
"Висельник" — это словесная игра, в которой один игрок загадывает слово, а другой пытается его угадать, предлагая буквы.

Правила:
    Программа выбирает слово и обозначает количество букв черточками.
    Угадывающий предлагает буквы. Если буква есть в слове, она открывается; если нет — добавляется часть тела к висельнику.
    Цель — угадать слово до завершения рисунка висельника (обычно 6-7 частей тела).
---
'''
maximum_count_attempts = 7
hangman_states = (
    '''
      -----
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      -----
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    '''
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''',
    '''
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    '''
)


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


def is_used_letter(set_of_words: set[str], letter: str) -> bool:
    return letter in set_of_words


def print_game_description() -> None:
    print(game_description)


def is_contains(word: str, letter: str) -> bool:
    return letter in word


def is_letter(symbol: str) -> bool:
    return symbol.isalpha() and len(symbol) == 1


def open_letter_in_user_word(secret_word: str,
                             user_word: str,
                             letter: str) -> str:
    user_word_list = list(user_word)
    for index, l in enumerate(secret_word):
        if letter == l:
            user_word_list[index] = letter
    return ''.join(user_word_list)


def print_game_information(user_word: str,
                           used_words: set[str],
                           attempts: int) -> None:
    print(f'''
Состояние висельника:
{hangman_states[attempts - 1]}
Использованные буквы: {', '.join(used_words)}
Осталось попыток: {maximum_count_attempts - attempts}
Ваше слово: {user_word}
    ''')