import re

verb_regexp = '(([а-яА-Я]{1,}[аеиоуыюя]{1}(ть|чь)(ся){0,1}|(сь){0,1}})|([а-яА-Я]{1,}[бвгджзйклмнпрстфхцчшщ]{1}(ти)))'
proverb_regexp = '(([а-яА-Я-]{1,}[бвгджзйклмнпрстфхцчшщ]{1}[оеуа]{1})|([а-яА-Я-]{1,}[чш]{1}ь)|(уж|замуж|невтерпеж|настежь))'
spaces_regexp = '[\s\n]{1,}'
general_regexp = re.compile('(' + spaces_regexp + verb_regexp + spaces_regexp + proverb_regexp + spaces_regexp + ')')
general_inverted_regexp = re.compile('('+ spaces_regexp + proverb_regexp + spaces_regexp + verb_regexp + spaces_regexp + ')')

f = open('./res/veldt.txt', mode='r', encoding='utf-8')
test_text = f.read()
f.close()
result = []
for match in general_regexp.finditer(test_text):
    result.append(match.group(1))
for match in general_inverted_regexp.finditer(test_text):
    result.append(match.group(1))
with open('./out/verb+proverb_result.txt', mode='w', encoding='utf-8') as f:
    for res in result:
        f.write(res.strip() + '\n')
