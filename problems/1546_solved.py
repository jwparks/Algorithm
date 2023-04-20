N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
modified_scores = []
for score in scores:
    modified_scores.append(score/max_score)
print(100*sum(modified_scores)/N)