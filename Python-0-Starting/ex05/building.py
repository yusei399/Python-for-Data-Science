import sys
import string

def count_characters(text):
    """
    Count the occurrences of different types of characters in the given text.

    Args:
    text (str): The input text to count characters from.

    Returns:
    dict: A dictionary containing the counts of uppercase letters, lowercase letters,
    punctuation marks, digits, and spaces.
    """
    if not text:
        return {}

    counts = {
        "upper letters": sum(1 for char in text if char.isupper()),
        "lower letters": sum(1 for char in text if char.islower()),
        "punctuation marks": sum(1 for char in text if char in string.punctuation),
        "spaces": sum(1 for char in text if char == ' '),  # 修正: スペースのみをカウント
        "digits": sum(1 for char in text if char.isdigit()),
    }

    return counts

def main():
    """
    Main function of the program.
    """
    try:
        # 引数が2つ以上ある場合にエラー
        if len(sys.argv) > 2:
            raise AssertionError("More than one argument is provided.")
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            text = input("What is the text to count?\n")

        # 文字カウントの取得
        character_counts = count_characters(text)

        # 文字の総数計算
        total_characters = sum(character_counts.values())

        print(f"The text contains {total_characters} characters:")
        for category, count in character_counts.items():
            print(f"{count} {category}")

    except EOFError:
        pass

if __name__ == "__main__":
    main()



