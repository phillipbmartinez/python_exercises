def reverseString(text):
    text_list = list(text)
    if len(text_list) == 0:
        return ""

    for char in range(len(text_list) // 2):
        mirror_char = len(text_list) - 1 - char
        text_list[char], text_list[mirror_char] = text_list[mirror_char], text_list[char]

    final_list = "".join(text_list)
    return final_list

assert reverseString('Hello') == 'olleH'
assert reverseString('') == ''
assert reverseString('aaazzz') == 'zzzaaa'
assert reverseString('xxxx') == 'xxxx'
print("All tests passed.")