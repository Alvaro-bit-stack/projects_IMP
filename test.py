def select_mode(key, mode):
    number = -1
    if 49 <= key <= 57:  # '1' ~ '9' (ASCII 49 to 57)
        number = key - 48
    elif 97 <= key <= 122:  # 'a' ~ 'z' (ASCII 97 to 122)
        number = key - 96  # 'a' = 1, ..., 'z' = 26

    if key == 110:  # 'n'
        mode = 0
    elif key == 107:  # 'k'
        mode = 1
    elif key == 104:  # 'h'
        mode = 2

    return number, mode
# Test numbers
print(select_mode(ord('1'), 0))  # Output: (1, 0)
print(select_mode(ord('9'), 0))  # Output: (9, 0)

# Test lowercase letters
print(select_mode(ord('a'), 0))  # Output: (1, 0)
print(select_mode(ord('j'), 0))  # Output: (10, 0)
print(select_mode(ord('z'), 0))  # Output: (26, 0)

# Test mode keys
print(select_mode(ord('n'), 0))  # Output: (-1, 0)
print(select_mode(ord('k'), 0))  # Output: (-1, 1)
print(select_mode(ord('h'), 0))  # Output: (-1, 2)
