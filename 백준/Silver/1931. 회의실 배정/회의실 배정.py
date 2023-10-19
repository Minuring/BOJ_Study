import sys

N = int(sys.stdin.readline())
meetings = []
for _ in range(N) :
    meetings.append(list(map(int, sys.stdin.readline().split())))
meetings.sort(key=lambda x:x[0])
meetings.sort(key=lambda x:x[1])
#(3,4)와 (4,4)가 있다고 가정하면 (4,4)가 먼저 선택되면 회의 개수가 한 개 적다.
#그래서 시작시간 순 정렬을 먼저 하고, 종료시간 순 정렬을 한다.

ans = [meetings[0][1]] #제일 빨리 끝나는 회의의 종료시간 먼저 넣고시작
for i in range(1, len(meetings)):
    if meetings[i][0] >= ans[-1] : #현재 가장 마지막에 끝나는 회의의 종료시간 이후면
        ans.append(meetings[i][1])

print(len(ans))