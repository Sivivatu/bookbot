def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


letters = (
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
)


def get_chars_dict(string: str) -> dict[str, int]:
    chars: dict[str, int] = {}

    for character in string:
        # if character in letters:
        lower: str = character.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    return chars
