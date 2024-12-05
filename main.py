def main():
    file_paths = "books/frankenstein.txt"
    with open(file_paths) as f:
        file_contents = f.read()

        print(count_words(file_contents))

def count_words(words):
    content = words.split()
    return len(content)


main()
