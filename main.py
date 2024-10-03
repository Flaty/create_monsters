from file_operations import render_template
from faker import Faker
from random import randint, sample
import os

skills = ['Стремительный прыжок', 'Электрический выстрел', 'Ледяной удар',
          'Стремительный удар', 'Кислотный взгляд', 'Тайный побег',
          'Ледяной выстрел', 'Огненный заряд']


letter_mapping = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}
runic_skills = []


def change_letter(letter_skill, mapping):

    word_list = []
    word = []
    for word_skill in letter_skill:
        letters = []
        for letter in word_skill:
            for map, let in mapping.items():
                if letter == map:
                    letter = let
            letters.append(letter)
        word = ''.join(letters)
        word_list.append(word)

    return word_list


def main():
    runic_skills = change_letter(skills, letter_mapping)
    fake = Faker('ru_RU')

    if not os.path.exists(r'output\svg'):
        os.makedirs(r'output\svg')

    for i in range(10):
        fake_skill_1, fake_skill_2, fake_skill_3 = sample(runic_skills, 3)
        runic_skills = sample(change_letter(skills, letter_mapping), 3)
        render_template(r'src\charsheet.svg', fr'output\svg\output-{i+1}.svg',
        {'first_name': fake.first_name(),
         'last_name':  fake.last_name(),
         'job': fake.job(),
         'town': fake.city(),
         'strength': randint(3, 18),
         'agility': randint(3, 18),
         'endurance': randint(3, 18),
         'intelligence': randint(3, 18),
         'luck': randint(3, 18),
         'skill_1': fake_skill_1,
         'skill_2': fake_skill_2,
         'skill_3': fake_skill_3})


if __name__ == '__main__':
    main()
