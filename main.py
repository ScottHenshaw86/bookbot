def count_words(str):
    return len(str.split())


def get_letter_counts(str):
    count_dict = {}
    for c in str:
        c = c.lower()
        if c not in "abcdefghijklmnopqrstuvwxyz":
            continue
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    count_list = list(count_dict.items())
    count_list.sort(key=lambda a: a[1], reverse=True)
    return count_list


def generate_report(file_path, word_count, letter_counts):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for letter in letter_counts:
        print(f"The '{letter[0]}' character was found {letter[1]} times")

    print("--- End report ---")


file_path = "books/frankenstein.txt"
with open(file_path) as f:
    file_contents = f.read()

    word_count = count_words(file_contents)
    letter_counts = get_letter_counts(file_contents)

    generate_report(file_path, word_count, letter_counts)
