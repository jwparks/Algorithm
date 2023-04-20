characters = list(input().lower())
unique_char = list(set(characters))

counts = []
for u, char in enumerate(unique_char):
    counts.append(characters.count(char))
indices = [idx for idx, item in enumerate(counts) if item == max(counts)]
if len(indices) > 1:
    print('?')
else:
    print(unique_char[indices[0]].upper())