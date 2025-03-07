import sys

n = int(sys.argv[i])

ruler = ' '
for i in range(1, n + 1):
    ruler = ruler + str(i) + ruler
print(ruler)