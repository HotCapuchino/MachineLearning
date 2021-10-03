import re

word = ''
not_compatible_regexp = re.compile('([А-яА-Я]{1,})')
syllable_regexp = re.compile('([бвгджзйклмнпрстфхцчшщъь]{0,}[аеёиоуыэюя][бвгджзйклмнпрстфхцчшщъь]{0,1})')

while not len(word):
    word = input('Введите слово на русском языке: ')
    if not re.search(not_compatible_regexp, word):
        word = ''

syllables = []
while word:
    last_syllable = re.search(syllable_regexp, word)
    if not last_syllable and len(syllables) > 0:
        syllables[len(syllables) - 1] += word
        word = ''
    else:
        syllables.append(last_syllable.group(1))
        word = re.sub(last_syllable.group(1), '', word)
print(syllables)