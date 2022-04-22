import re
from pprint import pprint

ru_re = re.compile(r"^[а-яА-Я,.:!?'()0-9 ]+$")
en_re = re.compile(r"^[a-zA-z,.:!?'()0-9 ]+$")
with open('C:\\Users\\bro\\Downloads\\russkoangliiskii_razgovornik2.txt', 'r', encoding='utf-8') as file:
    ru_phrases = []
    en_phrases = []
    lines = file.read().split(' \n')[::-1]
    for index, line in enumerate(lines):
        print(line)
    #     line = line.strip()
    #     is_ru_phrase = bool(ru_re.search(line))
    #     is_en_phrase = bool(en_re.search(line))
    #
    #     if is_en_phrase:
    #         if not len(en_phrases) or not en_re.search(lines[index - 1]):
    #             en_phrases.append(line)
    #         else:
    #             en_phrases[-1] += f' {line}'
    #
    #     if is_ru_phrase:
    #         if :
    #             ru_phrases.append(line)
    #         else:
    #             ru_phrases[-1] += f' {line}'

# print(ru_phrases)
