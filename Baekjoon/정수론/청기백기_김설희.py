n = int(input())
print(int(n**0.5))

'''
0 0 0 0 0 0 0 0 0 0  초기값

1 1 1 1 1 1 1 1 1 1  1의 배수 10개  1개만 있으면 1
1 0 1 0 1 0 1 0 1 0  2의 배수 5개   2개만 있으면 1
1 0 0 0 1 1 1 0 0 0  3의 배수 4개   3개만 있으면 1
1 0 0 1 1 1 1 1 0 0  4의 배수 6개   4개만 있으면 2
1 0 0 1 0 1 1 1 0 1  5의 배수 6개   5개만 있으면 2
1 0 0 1 0 0 1 1 0 1  6의 배수 5개   6개만 있으면 2
1 0 0 1 0 0 0 1 0 1  7의 배수 4개   7개만 있으면 2
1 0 0 1 0 0 0 0 0 1  8의 배수 3개   8개만 있으면 2
1 0 0 1 0 0 0 0 1 1  9의 배수 4개   9개만 있으면 3
1 0 0 1 0 0 0 0 1 0  10의 배수 3개  10개만 있으면 3
'''
