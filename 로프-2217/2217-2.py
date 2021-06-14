import sys
In = sys.stdin.readline

def main():
    n = int(In())
    rope = [0] * 10001
    print(rope)
    for _ in range(n):
        rope[int(In())] += 1
    m, s = 0, 0
    for x in range(10000,-1,-1):
        s += rope[x]
        m = max(m, x * s)
    print(m)
main()