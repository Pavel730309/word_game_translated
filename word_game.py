import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        word = soup.find("div", id="random_word").text.strip()
        definition = soup.find("div", id="random_word_definition").text.strip()
        return {"english_words": word, "word_definition": definition}
    except:
        print("Произошла ошибка")
        return None

def word_game():
    translator = Translator()
    print("Добро пожаловать в игру!")

    while True:
        data = get_english_words()
        if not data:
            continue

        word_en = data["english_words"]
        definition_en = data["word_definition"]

        try:
            word_ru = translator.translate(word_en, dest="ru").text
            definition_ru = translator.translate(definition_en, dest="ru").text
        except Exception as e:
            print("Ошибка перевода:", e)
            continue

        print(f"Значение на русском: {definition_ru}")
        user = input("Что это за слово (по-русски)? ")

        if user.lower() == word_ru.lower():
            print("Все верно!")
        else:
            print(f"Неверно. Было загадано: {word_ru} ({word_en})")

        again = input("Сыграем еще раз? (y/n): ")
        if again.lower() != "y":
            print("Спасибо за игру!")
            break

word_game()
