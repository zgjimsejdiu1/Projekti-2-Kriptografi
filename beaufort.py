def beaufort(text, key):
    result = ""
    key_len = len(key)
    j = 0

    for char in text:
        p = char.upper()

        if not p.isalpha():
            result += char
            continue

        k = key[j % key_len].upper()

        c = chr(((ord(k) - ord('A')) - (ord(p) - ord('A')) + 26) % 26 + ord('A'))
        result += c
        j += 1

    return result


def main():
    while True:
        print("\n1. Encrypt\n2. Decrypt\n3. Exit")
        choice = input("Choice: ")

        if choice in ["1", "2"]:
            text = input("Text: ")
            key = input("Key: ")

            print("Result:", beaufort(text, key))

        elif choice == "3":
            break


if __name__ == "__main__":
    main()