import tensorflow as tf


def parse_words(word_list, allowed_letters, word_length):
    valid_words = []

    for word in word_list:
        word = word.strip().upper()
        if len(word) == word_length and all(letter in allowed_letters for letter in word):
            if len(set(word)) == word_length:
                valid_words.append(word)

    return valid_words


def main():
    allowed_letters = 'ABCDEFGHIK'
    word_length = 7
    all_valid_words = []

    for dataset_number in range(1, 13):
        dataset_file = f'dataset_{dataset_number}.txt'
        with open(dataset_file, 'r') as file:
            word_list = file.readlines()

        valid_words = parse_words(word_list, allowed_letters, word_length)
        all_valid_words.extend(valid_words)

    print("Total number of valid words:", len(all_valid_words))
    # Perform further processing with TensorFlow if needed


if __name__ == "__main__":
    main()
