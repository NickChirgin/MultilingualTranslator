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
    result = []
    example_list = []
    original_list = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    print(f"Hello, you're welcome to the translator. Translator supports: {ln_dict}")
    language1 = int(input("Type the number of your language:"))
    language_orgnl = ln_dict.get(language1)
    language_tranlate_to = int(input("Type the number of language you want to translate to or '0' to translate to all languages:"))
    word = input("Type the word you want to translate:")
    if language_tranlate_to == 0:
        all_languages(language_orgnl, ln_dict, word, headers)
    else:
        with open(f"{word}.txt", "w", encoding="utf-8") as f:
            language_tranlate_to = ln_dict.get(language_tranlate_to)
            url = link(language_orgnl.lower(), language_tranlate_to.lower(), word)
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")
            for item in soup.select('#translations-content .translation'):
                result.append(item.text.strip())
            for example in soup.select('#examples-content .example .trg .text'):
                example_list.append(example.text.strip())
            for original in soup.select('#examples-content .example .src .text, #examples-content .example .src .text-nikkud'):
                original_list.append(original.text.strip())
            print(f"{language_tranlate_to} Translations:")
            f.writelines(f"{language_tranlate_to} Translations:" + "\n")
            print(result[0])
            f.writelines(result[0] + "\n")
            print(f"{language_tranlate_to} Examples:")
            f.writelines(f"{language_tranlate_to} Examples:" + "\n")
            print(original_list[0])
            f.writelines(original_list[0] + "\n")
            print(example_list[0])
            f.writelines(example_list[0] + "\n")

def output(chosen_language, chosen_word):
    print(f"You chose {chosen_language} as the language to translate {chosen_word} to.")


def link(ln1, ln2, word):
    url = f"https://context.reverso.net/translation/{ln1}-{ln2}/{word}"
    return url


def all_languages(original_ln, ln_dict, letter, headers):
    with open(f"{letter}.txt", "w", encoding="utf-8") as f:
        f.truncate(0)
        for i in range(1, 14):
            list_example = []
            list_orig = []
            result_list = []
            translate_ln = ""
            if ln_dict.get(i) == original_ln:
                continue
            translate_ln = ln_dict.get(i)
            url = link(original_ln.lower(), translate_ln.lower(), letter)
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")
            for item in soup.select('#translations-content .translation'):
                result_list.append(item.text.strip())
            for example in soup.select('#examples-content .example .trg .text'):
                list_example.append(example.text.strip())
            for original in soup.select('#examples-content .example .src .text, #examples-content .example .src .text-nikkud'):
                list_orig.append(original.text.strip())
            print(f"{translate_ln} Translations:")
            f.writelines(f"{translate_ln} Translations:" + "\n")
            print(result_list[0])
            f.writelines(result_list[0] + "\n")
            print(f"{translate_ln} Examples:")
            f.writelines(f"{translate_ln} Examples:" + "\n")
            print(list_orig[0])
            f.writelines(list_orig[0] + "\n")
            print(list_example[0])
            f.writelines(list_example[0] + "\n")


if __name__ == "__main__":
    main()


