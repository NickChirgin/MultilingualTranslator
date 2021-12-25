import requests
from bs4 import BeautifulSoup
import string


def main():
    language = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
    word = input("Type the word you want to translate:")
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = ""
    ln_dict = { "en" : "English", "fr": 'French'}
    result = []
    example_list = []
    original_list = []
    if language == "en":
        url = f"https://context.reverso.net/translation/french-english/{word}"
    else:
        url = f"https://context.reverso.net/translation/english-french/{word}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    output(language, word)
    if r.status_code == 200:
        print(200, "OK")

    for item in soup.select('#translations-content .translation'):
        result.append(item.text.strip())
    for example in soup.select('#examples-content .example .trg .text'):
        example_list.append(example.text.strip())
    for original in soup.select('#examples-content .example .src .text, #examples-content .example .src .text-nikkud'):
        original_list.append(original.text.strip())
    print(f"{ln_dict.get(language)} Translations:")
    for i in result:
        print(i)
    print(f"{ln_dict.get(language)} Examples:")
    for i in range(0, 5):
        print(original_list[i])
        print(example_list[i])


def output(chosen_language, chosen_word):
    print(f"You chose {chosen_language} as the language to translate {chosen_word} to.")


if __name__ == "__main__":
    main()


