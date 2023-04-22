N = int(input())
words_count = []
words = {}
for _ in range(N):
    word = input()
    words_count.append(len(word))
    try:
        words[len(word)].append(word)
    except:
        words[len(word)] = [word]

for i, n in enumerate(sorted(set(words_count))):
    for j in sorted(set(words[n])):
        print(j)
