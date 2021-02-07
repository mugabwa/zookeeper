# Write your code here
from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams, trigrams
from collections import Counter
from random import choices, choice
import re


filename = input()
tk = WhitespaceTokenizer()
with open(filename, 'r', encoding='utf-8') as fc:
    cops = fc.readlines()
cops1 = " ".join(cops)
copsx = tk.tokenize(cops1)
tricops = list(trigrams(copsx))
bicops = list(bigrams(copsx))

tricop_dict = {}
for head1, head2, tail in tricops:
    head = head1 + " " + head2
    tricop_dict.setdefault(head, []).append(tail)
regex1 = r'^[A-Z][a-z\']*?$'
regex2 = r'^[A-z\'-]*?$'
regex3 = r'^[A-z\'-]*?[.!?]$'
regex4 = r'^[A-Z][A-z\' ]*?$'
new_elements = ''

for _xelem in range(len(tricop_dict)):
    start1 = choice(tricops)
    if re.match(regex1, start1[0]) and re.match(regex2, start1[1]):
        new_elements = start1[0] + " " + start1[1]
        break

tkholder = ""
_a = 0
while _a < 10:
    new_count = Counter(tricop_dict[new_elements])
    sentence = [new_elements.split()[0], new_elements.split()[1]]
    for _x in range(8):
        if _x < 4:
            for _y in range(len(new_count.values())):
                new_word = choices(list(new_count.keys()), weights=list(new_count.values()), k=2)
                if not re.match(regex3, new_word[0]):
                    sentence.append(new_word[0])
                    tkholder = sentence[-2] + " " + new_word[0]
                    new_count = Counter(tricop_dict[tkholder])
                    break
        elif 4 <= _x < 7:
            new_word = choices(list(new_count.keys()), weights=list(new_count.values()), k=1)
            if re.match(regex3, new_word[0]):
                sentence.append(new_word[0])
                break
            else:
                sentence.append(new_word[0])
                tkholder = sentence[-2] + " " + new_word[0]
                new_count = Counter(tricop_dict[tkholder])
        else:
            for _z in range(len(new_count.values())):
                new_word = choices(list(new_count.keys()), weights=list(new_count.values()), k=4)
                if re.match(regex3, new_word[0]):
                    sentence.append(new_word[0])
                    break
    for _xelem in range(len(tricops)):
        start1 = choice(tricops)
        if re.match(regex1, start1[0]) and re.match(regex2, start1[1]):
            new_elements = start1[0] + " " + start1[1]
            break
    if len(sentence) < 5 or not re.match(regex3, sentence[-1]):
        pass
    else:
        _a += 1
        print(" ".join(sentence))


# cops_dict = {}
# for head, tail in bicops:
#     cops_dict.setdefault(head, []).append(tail)
# regex1 = r'^[A-Z][a-z\']*?$'
# regex2 = r'^[A-z\'-]*?$'
# regex3 = r'^[A-z\'-]*?[.!?]$'
# new_elements = ''
# for _xelem in range(len(bicops)):
#     start1 = choice(bicops)
#     if re.match(regex1, start1[0]):
#         new_elements = start1[0]
#         break
#     elif re.match(regex1, start1[1]):
#         new_elements = start1[1]
#         break
# new_count = Counter(cops_dict[new_elements])
# for _a in range(10):
#     sentence = []
#     sentence.append(new_elements)
#     for _x in range(9):
#         if _x < 3:
#             for _y in range(len(new_count.values())):
#                 new_word = choices(list(new_count.keys()), weights=list(new_count.values()), k=2)
#                 if not re.match(regex3, new_word[0]):
#                     sentence.append(new_word[0])
#                     break
#         elif 3 <= _x < 8:
#             new_word = choices(list(new_count.keys()), weights=list(new_count.values()), k=1)
#             if re.match(regex3, new_word[0]):
#                 sentence.append(new_word[0])
#                 break
#             else:
#                 sentence.append(new_word[0])
#         else:
#             for _z in range(len(new_count.values())):
#                 new_word = choices(list(new_count.keys()), weights=list(new_count.values()), k=4)
#                 if re.match(regex3, new_word[0]):
#                     sentence.append(new_word[0])
#                     break
#     for _xelem in range(len(bicops)):
#         start1 = choice(bicops)
#         if re.match(regex1, start1[0]):
#             new_elements = start1[0]
#             break
#         elif re.match(regex1, start1[1]):
#             new_elements = start1[1]
#             break
#     print(" ".join(sentence))
