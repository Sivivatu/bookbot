import sys
from stats import get_num_words, get_book_text, get_chars_dict, chars_dict_to_sorted_list

inputs: list[str] = sys.argv


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: uv run main.py <path_to_book>")
        return sys.exit(1)
    path_to_file = sys.argv[1]
    book_text: str = get_book_text(path_to_file)
    book_count: int = get_num_words(book_text)
    character_count: dict[str, int] = get_chars_dict(book_text)
    sorted_chars_list: list[tuple[str, int]] = chars_dict_to_sorted_list(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {book_count} total words")
    print("--------- Character Count -------")
    for c, count in sorted_chars_list:
        print(f"{c}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
