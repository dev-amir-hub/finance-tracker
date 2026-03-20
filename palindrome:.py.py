def is_palindrome(text):
    cleaned = ''
    for char in text:
        if char.isalpha():
            cleaned += char.lower()
    return cleaned == cleaned[::-1]


def count_palindromes(words):
    count = 0
    for word in words:
        if is_palindrome(word):
            count += 1
    return count

