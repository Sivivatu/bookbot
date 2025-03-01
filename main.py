from stats import get_num_words, get_book_text


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


def unique_characters(string) -> dict:
    chars = {}

    for character in string:
        if character in letters:
            lower = character.lower()
            if lower in chars:
                chars[lower] += 1
            else:
                chars[character] = 1
    return chars


def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    book_count = get_num_words(book_text)
    character_count = unique_characters(book_text)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{book_count} words found in the document")
    print("\n")
    for c in sorted(character_count, key=character_count.get, reverse=True):
        print(f"The character '{c}' was found {character_count[c]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
