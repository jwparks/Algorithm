from itertools import combinations
from copy import copy
L, C = map(int, input().split())
characters = input().split()

vowels = []
consonants = []
for ch in characters:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(ch)
    else:
        consonants.append(ch)

consonant_set = list(combinations(consonants, 2))
passwords = []
for v, vowel in enumerate(vowels):
    for c, consonant in enumerate(consonant_set):
        vowel_remains = copy(vowels)
        consonant_remains = copy(consonants)
        vowel_remains.remove(vowel)
        consonant_remains.remove(consonant[0])
        consonant_remains.remove(consonant[1])
        remains = vowel_remains + consonant_remains
        R = L - 3
        remain_set = list(combinations(remains, R))
        for r, remain in enumerate(remain_set):
            password = [vowel, consonant[0], consonant[1]] + [remain[i] for i in range(len(remain))]
            passwords.append(''.join(sorted(password)))
passwords = sorted(set(passwords))
for password in passwords:
    print(password)