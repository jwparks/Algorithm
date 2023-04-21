table = {'AA' : 'A',
         'GA' : 'C',
         'CA' : 'A',
         'TA' : 'G',
         'AG' : 'C',
         'GG' : 'G',
         'CG' : 'T',
         'TG' : 'A',
         'AC' : 'A',
         'GC' : 'T',
         'CC' : 'C',
         'TC' : 'G',
         'AT' : 'G',
         'GT' : 'A',
         'CT' : 'G',
         'TT' : 'T',
        }

N = int(input())
DNA = list(input().rstrip())
while len(DNA) > 1:
    base_n = DNA.pop()
    base_n1 = DNA.pop()
    newbase = table[base_n1+base_n]
    DNA.append(newbase)
print(DNA.pop())