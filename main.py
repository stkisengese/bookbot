
def main():
    file_paths = "books/frankenstein.txt"
    with open(file_paths) as f:
        file_contents = f.read()

        print(count_words(file_contents))
        print(f"Count Characters: {count_characters(file_contents)}")

def count_words(words):
    content = words.split()
    return len(content)

def count_characters(text):
    char_counts = {}
    lower_text = text.lower()
    for char in lower_text:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts


main()
