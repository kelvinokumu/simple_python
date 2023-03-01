from collections import Counter


def read_file_content(filename):
    # [assignment] Add your code here
    textfile = open(filename, "r")
    data = textfile.read()

    return data


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    words_counted = dict(Counter(text.split()))
    print(words_counted)

    return words_counted


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count_words()
