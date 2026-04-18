import math


def clean_text(text):
    return "".join(c.upper() for c in text if c.isalpha())



def diagonal_encrypt(text):
    text = clean_text(text)
    length = len(text)

    size = 1
    while size * size < length:
        size += 1

    
    grid = [['X' for _ in range(size)] for _ in range(size)]

    index = 0

    
    for i in range(size):
        for j in range(size):
            if index < length:
                grid[i][j] = text[index]
                index += 1

    
    result = ""

    for k in range(2 * size):
        for i in range(size):
            j = k - i
            if 0 <= j < size:
                result += grid[i][j]

    return result



def diagonal_decrypt(text):
    text = clean_text(text)
    length = len(text)

    size = 1
    while size * size < length:
        size += 1

    grid = [['X' for _ in range(size)] for _ in range(size)]

    index = 0

    
    for k in range(2 * size):
        for i in range(size):
            j = k - i
            if 0 <= j < size and index < length:
                grid[i][j] = text[index]
                index += 1

    
    result = ""
    for i in range(size):
        for j in range(size):
            if grid[i][j] != 'X':
                result += grid[i][j]

    return result



def main():
    while True:
        print("\n===== DIAGONAL CIPHER =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Choice: ")

        if choice == "1":
            text = input("Text: ")
            print("Encrypted:", diagonal_encrypt(text))

        elif choice == "2":
            text = input("Text: ")
            print("Decrypted:", diagonal_decrypt(text))

        elif choice == "3":
            break


if __name__ == "__main__":
    main()

