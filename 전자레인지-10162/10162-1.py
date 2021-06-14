import sys
input = sys.stdin.readline


def main():
    num = int(input())
    cnt = []
    cnt.append(num//300)
    num %= 300
    cnt.append(num//60)
    num %= 60
    cnt.append(num//10)
    num %= 10
    if num != 0:
        print(-1)
        return
    for i in range(len(cnt)):
        print(cnt[i],end=" ")


main()
