# [Silver I] 회의실 배정 - 1931 

[문제 링크](https://www.acmicpc.net/problem/1931) 

### 성능 요약

메모리: 51900 KB, 시간: 264 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2023년 10월 19일 22:54:52

### 문제 설명

<p>한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.</p>

### 입력 

 <p>첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 2<sup>31</sup>-1보다 작거나 같은 자연수 또는 0이다.</p>

### 출력 

 <p>첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.</p>

### 문제 풀이

 <p>단 하나의 회의실에 최대한 많은 회의를 배정하기 위해서는 회의들이 <strong>빨리 끝나야 한다.</strong><br>
그래서 종료시간 기준으로 정렬을 해야하는데, 이 문제에서는 시작 하자마자 끝나는 회의가 있으므로 <br>
만약 (4,4)와 (3,4)가 있을 때 (4,4)가 먼저 배정되면 (3,4)를 먼저 배정했을 때보다 한 개 덜 배정하게 된다.<br>
따라서 시작시간순 정렬 후에 종료시간순 정렬을 한 후, 현재까지 종료시간과 다음 회의의 시작시간을 계속 비교한다.
</p>
