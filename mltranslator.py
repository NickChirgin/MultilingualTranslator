def main():
    language = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
    word = input("Type the word you want to translate:")
    output(language, word)


def output(chosen_language, chosen_word):
    print(f"You chose {chosen_language} as the language to translate {chosen_word} to.")


if __name__ == "__main__":
    main()


