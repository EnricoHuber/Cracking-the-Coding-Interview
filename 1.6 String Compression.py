"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def string_frequency(string):
    flag = False
    substring_frequencies = []
    letter_freq = 1
    for i in range(len(string)-1):
        if i == len(string)-2 and string[i] == string[i+1]:
            substring_frequencies.append((string[i]*(letter_freq+1), letter_freq+1))
            break
        elif i == len(string)-2 and string[i] != string[i+1]:
            substring_frequencies.append((string[i]*letter_freq, letter_freq))
            substring_frequencies.append((string[i+1], 1))
            break
        elif string[i+1] == string[i]:
            flag = True
            letter_freq += 1
            continue
        else:
            substring_frequencies.append((string[i]*letter_freq, letter_freq))
        letter_freq = 1
    return substring_frequencies, flag


def string_compressed(freq_dict):
    str_compressed = ''
    for substr_freq in freq_dict:
        str_compressed += substr_freq[0][0] + str(substr_freq[1])
    return str_compressed


def main():
    string_input = 'aabcccccaaa'
    chars_frequencies, can_be_compressed = string_frequency(string_input)
    if not can_be_compressed:
        print(string_input)
    else:
        print(string_compressed(chars_frequencies))


if __name__ == "__main__":
    main()