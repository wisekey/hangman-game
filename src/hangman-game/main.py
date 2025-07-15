path_to_file = 'src/hangman-game/ru_nouns.txt'


def get_nouns_from_file(filename: str) -> list[str]:
    with open(filename, mode='r', encoding='utf-8') as file:
        return [noun.strip() for noun in file]
    

def print_welcome_message() -> None:
    print('Добро пожаловать в игру "Висельник"')

