def break_words(stuff):
    words = stuff.split()
    return words


def sort_words(words):
    return sorted(words)


def print_first_word(words):
    word = words.pop(0)
    return word


def print_last_word(words):
    word = words.pop(-1)
    return word


def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    words = break_words(sentence)
    first_word = print_first_word(words)
    last_word = print_last_word(words)
    return first_word, last_word


def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    sorted_first_word = print_first_word(words)
    sorted_last_word = print_last_word(words)
    return sorted_first_word, sorted_last_word


# Take a sentence from user
sentence = input("Enter a sentence here :")

# Split the sentence in words
words = break_words(sentence)
print(f"\nThe splited sentence in words is : {words}")

# Lets sort the words.
sorted_words = sort_words(words)
print(f"\nThe words sorted in order : {sorted_words}")

# Printing the first word
first = print_first_word(words)
print(f"\nThe first word is : {first}")

last = print_last_word(words)
print(f"\nThe last word is: {last}")

# Words left after popping
print(f"\nWords left after popping first and last word are : {words}")

# first and last of sorted words
sorted_first = print_first_word(sorted_words)
print(f"\nThe first word of sorted words is : {sorted_first}")

sorted_last = print_last_word(sorted_words)
print(f"\nThe last word of sorted words is : {sorted_last}")

# Words left after popping first and last words
print(f"\nWords left after popping first and last soretd word are : {sorted_words}")

# Lets assign the sentence to sorted_words again
sorted_words = sort_sentence(sentence)
print(f"\nNow the sorted words are : {sorted_words}")

# Finding out first and last of normal and sorted words
print("\nThe first and last words >>>")
first, last = print_first_and_last(sentence)
print(f"The first word is : {first} \nThe last word is : {last}")

print("\nThe first and last of the soretd words >>>")
sorted_first_word, sorted_last_word = print_first_and_last_sorted(sentence)
print(f"The first word is : {sorted_first_word} \nThe last word is : {sorted_last_word}")
