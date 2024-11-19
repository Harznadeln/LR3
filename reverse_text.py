def reverse_string(text):
    return text[::-1]

if __name__ == "__main__":
    input_text = input("Введіть текст: ")
    print("Віддзеркалений текст:", reverse_string(input_text))