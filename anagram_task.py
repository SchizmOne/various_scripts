"""Given the following string: "race bear thing care keen trap tweet earth knee heart  neek tewt"

Write a function which takes as input this string and returns as a result a dictionary of items,
which contains the words from the given string as keys and as values a list with its anagrams from
within the input string, if there are any (if there are not, an empty list shall be used as value for
the specific keyword). Anagrams already found for a specific word shall not be considered new keys in
the dictionary. Duplicate words will not be added as new keys or values.

Input Example:
s = "race bear thing care keen trap tweet earth knee heart  neek tewt"

Output Example:
{'race': ['care'], 'bear': [] 'thing': [], 'keen': ['knee', 'neek'], 'trap': [], 'tweet': [], 'earth': ['heart'], 'tewt': []}
"""


def is_anagram(word1: str, word2: str) -> bool:
    """Checks if word1 and word2 are anagrams of each other.

    Args:
        word1 (str): First word to check.
        word2 (str): Second word to check.
    Returns:
        True if both words are anagrams, False otherwise.
    """
    if (len(word1) != len(word2)) or not word1 or not word2:
        return False
    word2_chars = list(word2)
    for char in word1:
        if char not in word2_chars:
            return False
        word2_chars.remove(char)
    return len(word2_chars) == 0


def check_string_for_anagrams(string_to_check: str) -> dict[str, list[str]]:
    """Checks the words in the given string for possible anagrams.

    Args:
        string_to_check (str): String to be checked.
    Returns:
        Dictionary of words as keys and list of their anagrams in values.
    """
    words = string_to_check.lower().split(' ')
    unique_words = set()
    anagrams_map = {}
    for word_to_check in words:
        if not word_to_check.isalpha() or (word_to_check in unique_words):
            continue
        anagrams_map[word_to_check] = []
        for word_to_compare in words:
            if word_to_check != word_to_compare and is_anagram(word_to_compare, word_to_check):
                anagrams_map[word_to_check].append(word_to_compare)
                unique_words.add(word_to_compare)
    return anagrams_map


if __name__ == '__main__':
    test_string = input('Please, write a string to check for anagrams:\n')
    print(f"\nGot you. Here's the results:\n{check_string_for_anagrams(test_string)}")
