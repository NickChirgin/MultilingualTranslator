import requests
from bs4 import BeautifulSoup
import string


def main():
    ln_dict = {
        1: "Arabic",
        2: "German",
        3: "English",
        4: "Spanish",
        5: "French",
        6: "Hebrew",
        7: "Japanese",
        8: "Dutch",
        9: "Polish",
        10: "Portuguese",
        11: "Romanian",
        12: "Russian",
        13: "Turkish"
    }
    headers = {'User-Agent': 'Mozilla/5.0'}
    print(f"Hello, you're welcome to the translator. Translator supports: {ln_dict}")
    language1 = int(input("Type the number of your language:"))
    language_orgnl = ln_dict.get(language1)
    language_tranlate_to = int(input("Type the number of language you want to translate to:"))
    language_tranlate_to = ln_dict.get(language_tranlate_to)
    word = input("Type the word you want to translate:")

    url = ""

    result = []
    example_list = []
    original_list = []
    url = link(language_orgnl.lower(), language_tranlate_to.lower(), word)
    print(url)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    #output(language, word)
    if r.status_code == 200:
        print(200, "OK")

    for item in soup.select('#translations-content .translation'):
        result.append(item.text.strip())
    for example in soup.select('#examples-content .example .trg .text'):
        example_list.append(example.text.strip())
    for original in soup.select('#examples-content .example .src .text, #examples-content .example .src .text-nikkud'):
        original_list.append(original.text.strip())
    print(original_list)
    print(f"{language_tranlate_to} Translations:")
    for i in result:
        print(i)
    print(f"{language_tranlate_to} Examples:")
    if len(original_list) >= 5:
        for i in range(0, 5):
            print(original_list[i])
            print(example_list[i])
    else:
        for i in range(0, len(original_list) + 1):
            print(original_list[i])
            print(example_list[i])


def output(chosen_language, chosen_word):
    print(f"You chose {chosen_language} as the language to translate {chosen_word} to.")


def link (ln1, ln2, word):
    url = f"https://context.reverso.net/translation/{ln1}-{ln2}/{word}"
    return url


if __name__ == "__main__":
    main()


