def get_nouns_from_file(filename: str) -> list[str]:
    with open(filename, mode='r', encoding='utf-8') as file:
        return [noun.strip() for noun in file]