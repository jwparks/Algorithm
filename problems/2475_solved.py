numbers = list(map(int, input().split()))
check_number = 0
for n in numbers:
    check_number += n**2
print(check_number%10)