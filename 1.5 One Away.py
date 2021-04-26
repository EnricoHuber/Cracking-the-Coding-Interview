"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""
import string


def check_one_zero_away(str1, str2):
    if str1 == str2:
        return True

    for char in string.ascii_lowercase:
        if str1.replace(char, '') == str2 or str2.replace(char, '') == str1:
            return True

    if len(str1) == len(str2):
        for i in range(len(str1)-1):
            if str1.replace(str1[i], '') == str2.replace(str2[i], ''):
                return True


def main():
    string_input_1 = 'pale'
    string_input_2 = 'bale'     # Try also with ple, pales, bake (this should return False)
    if check_one_zero_away(string_input_1, string_input_2):
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
