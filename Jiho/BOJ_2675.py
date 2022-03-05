# 문자열 반복

# for _ in range(int(input())):
#     R, S = input().split()
#     for i in S:
#         P = i * int(R)
#         print(P, end='')
#     print()




for _ in range(int(input())):
    n, word = input().split()
    for i in word:
        print(i * int(n), end='')
    print()

    