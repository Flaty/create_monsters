from file_operations import render_template
from faker import Faker
from random import randint, sample
import os

SKILLS = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
    ]


LETTER_MAPPING = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}


def change_letter(skills, letter_mapping):

    transformed_skills = []
    for skill in skills:
        transformed_letters = []
        for letter in skill:
            letter = letter_mapping.get(letter, letter)
            transformed_letters.append(letter)
        transformed_skill = ''.join(transformed_letters)
        transformed_skills.append(transformed_skill)

    return transformed_skills


def main():
    runic_skills = change_letter(SKILLS, LETTER_MAPPING)
    fake = Faker('ru_RU')

    os.makedirs(os.path.join('output', 'svg'), exist_ok=True)

    for i in range(10):
        fake_skill_1, fake_skill_2, fake_skill_3 = sample(runic_skills, 3)

        render_template(
            os.path.join('src', 'charsheet.svg'),
            os.path.join('output', 'svg', f'output-{i+1}.svg'),
            {
                'first_name': fake.first_name(),
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
                'skill_3': fake_skill_3
            })


if __name__ == '__main__':
    main()
