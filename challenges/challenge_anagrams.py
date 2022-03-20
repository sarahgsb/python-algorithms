def selection_sort(string):
    word = list(string)

    for i in range(len(word)):
        min = i

        for j in range(i + 1, len(word)):
            if word[j] < word[min]:
                min = j

        word[min], word[i] = word[i], word[min]

    return word


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    if first_string == "" or second_string == "":
        return False
    if selection_sort(first_string.lower()) == selection_sort(
        second_string.lower()
    ):
        return True

    return False
