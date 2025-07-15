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


def print_winner_message(secret_word: str) -> None:
    print(f'Вы выиграли! Загаданное слово {secret_word}')
    

def start_game():
    from random import choice

    attemtps = 1
    nouns = get_nouns_from_file(path_to_file)
    secret_word = choice(nouns)
    user_word = '_' * len(secret_word)
    used_words = set()
    is_win = True

    while secret_word != user_word:
        if attemtps >= maximum_count_attempts:
            print('Вы проиграли')
            is_win = False
            break

        print_game_information(user_word, used_words, attemtps)
        letter = input('Введите предполагаемую букву:')

        if not is_letter(letter):
            print('Но это не буква! Попробуйте еще раз')
            continue

        if is_used_letter(used_words, letter):
            print('Буква уже была введена. Попробуйте другую')
            continue
        
        if is_contains(secret_word, letter):
            user_word = open_letter_in_user_word(secret_word, user_word, letter)
        else:
            attemtps += 1
            print('Такой буквы в слове нет')
        used_words.add(letter)
    
    if is_win:
        print_winner_message(secret_word)
    else:
        print_game_information(secret_word, used_words, attemtps)


def main() -> None:
    print_welcome_message()

    while True:
        print_menu()
        choice = input('Выберите опцию:')
        
        if choice == '1':
            print_game_description()
            continue
        elif choice == '2':
            start_game()
        elif choice == '3':
            print('Вы принудительно вышли из игры. До свидания!')
            break
        else:
            print('Вы выбрали неверную опцию! Попробуйте еще раз')


if __name__ == '__main__':
    main()