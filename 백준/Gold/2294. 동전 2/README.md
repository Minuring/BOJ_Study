# [Gold V] 동전 2 - 2294 

[문제 링크](https://www.acmicpc.net/problem/2294) 

### 성능 요약

메모리: 31120 KB, 시간: 248 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2023년 11월 13일 19:07:25

### 문제 설명

<p>n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.</p>

### 입력 

 <p>첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.</p>

### 출력 

 <p>첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.</p>

### 문제 풀이

<pre>dp 배열을 -1로 교환할 액수만큼 만든다.
1(원)부터 ,,, m원,,, M(원)까지 다음을 반복한다.
각각 액면가의 동전 액수 i에 대해, i >= m 일 때 (동전액면가가 현재 액수 이상일 때, 
즉 현재 i원짜리 동전으로 교환 가능할 때),  (*)**dp[m]과 dp[m-i]+1 중 최소값을 선택**한다.
즉 m원에서 i원 각각을 뺀 액면가들 중 최소 개수를 선택한다.

1~M원에 대해 각 액수마다 동전 액면가 개수 n만큼 반복한다. 따라서 시간복잡도는 O(nM)이다.

(*) Q. 액수가 크면 m-i가 작아지니까 최소값을 꼭 비교하지 않아도 최소값이 되는 것 아닌가?
    dp[m] = dp[m-i]+1로 최소값 비교를 하지 않고 갱신할 경우 :
    반례 : coin = [1,5,12] money = 15
    i=0(1원짜리)일때 dp[15] = dp[14]+1 = 3+1 = 4
    i=1(5원짜리)일때 dp[15] = dp[10]+1 = 2+1 = 3
    i=2(12원짜리)일때 dp[15] = dp[3]+1 = 3+1 = 4
    최적해 dp[15] = 3, 위 예에서 구한 해 : 4
    
</pre>