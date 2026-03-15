def palindrome(text):
    cleaned =''
    for char in text:
        if char.isalpha():
            cleaned+=char.lower()
    return cleaned==cleaned[::-1]
print(palindrome('лепс спел'))