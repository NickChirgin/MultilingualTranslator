import requests
from bs4 import BeautifulSoup
import string


def main():
    language = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
    word = input("Type the word you want to translate:")
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = ""
    ln_dict = { "en" : "english", "fr" : 'french'}
    result = []
    example_list = []
    if language == "en":
        url = f"https://context.reverso.net/translation/french-english/{word}"
    else:
        url = f"https://context.reverso.net/translation/english-french/{word}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    output(language, word)
    if r.status_code == 200:
        print(200, "OK")
    print("Translation")
    for item in soup.select('#translations-content .translation'):
        result.append(item.text.strip())
    for example in soup.select('#examples-content .example .trg .text'):
        example_list.append(example.text.strip())
    print(result)
    print(example_list)


def output(chosen_language, chosen_word):
    print(f"You chose {chosen_language} as the language to translate {chosen_word} to.")


if __name__ == "__main__":
    main()


