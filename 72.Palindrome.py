def is_palindrome(word):
    pos = -1
    for i in range(0, len(word) // 2):  # There's no need to check the complete string, just half of it
        if word[i] == word[pos]:
            pos -= 1
        else:
            print(f'{word} is NOT palindrome')
            return
    print(f'{word} is palindrome')


def is_palindrome_2(word):
    if word == word[::-1]:
        print(f'{word} is palindrome')
    else:
        print(f'{word} is NOT palindrome')


is_palindrome('house')
is_palindrome_2('house')
is_palindrome('bob')
is_palindrome_2('bob')
is_palindrome('anna')
is_palindrome_2('anna')
is_palindrome('john')
is_palindrome_2('john')
