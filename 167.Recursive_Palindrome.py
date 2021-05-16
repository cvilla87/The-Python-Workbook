def is_palindrome(string):
    if len(string) <= 1:
        return True
    return string[0] == string[len(string) - 1] and is_palindrome(string[1:len(string)-1])


for word in ('house', 'bob', 'anna', 'john'):
    if is_palindrome(word):
        print(f'{word} is palindrome')
    else:
        print(f'{word} is NOT palindrome')
