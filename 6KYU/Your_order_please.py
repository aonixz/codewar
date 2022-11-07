from typing import Optional


def extract_number(word: str) -> Optional[int]:
    for letter in word:
        if letter.isdigit():
            return int(letter)
    return None


def order(sentence: str) -> str:
    return ' '.join(sorted(sentence.split(), key=extract_number))