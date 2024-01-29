import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for i in range(1,N+1):
    dic[i] = input().rstrip()

dic2 = dict(zip(dic.values(),dic.keys()))
for _ in range(M):
    quest = input().rstrip()

    try:
        n = int(quest)
        print(dic[n])
    except:
        print(dic2[quest])