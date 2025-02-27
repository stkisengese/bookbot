from stats import count_words

def main():
    file_paths = "books/frankenstein.txt"
    with open(file_paths) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    # char_counts = count_characters(file_contents)

    # print_report(word_count, char_counts)
    print(f"{word_count} words found in the document")

main()
