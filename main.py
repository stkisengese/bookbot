import sys
from stats import count_words, count_characters, print_report

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    file_paths = sys.argv[1]
    with open(file_paths) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_counts = count_characters(file_contents)

    print_report(word_count, char_counts)


main()
