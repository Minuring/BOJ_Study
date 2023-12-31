# [Gold V] 별 찍기 - 10 - 2447 

[문제 링크](https://www.acmicpc.net/problem/2447) 

### 성능 요약

메모리: 40604 KB, 시간: 60 ms

### 분류

분할 정복, 재귀

### 문제 설명

<p>재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.</p>

<p>크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.</p>

<pre>***
* *
***</pre>

<p>N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3<sup>k</sup>이며, 이때 1 ≤ k < 8이다.</p>

### 출력 

 <p>첫째 줄부터 N번째 줄까지 별을 출력한다.</p>

### 문제 풀이

<pre>
N == 3 인 레벨을 최소단위로 생각했습니다.
즉 N==3이면,
***
* *
***
를 반환합니다.


N==9이상 레벨)
문제의 별 패턴에서 "*"에 해당하는 부분을 더 깊은 레벨 ( N//3 ) 단위로 생각합니다.
즉 line6의 stars를 문제의 패턴대로 반복시켜 반환합니다.

N==3레벨 )
N==3 레벨에서 호출된 N==1 레벨은 "*"를 리턴하기 때문에, stars는 "*" 입니다.
line9~14를 거친 후 L의 내용은 ['***', '* *', '***'] 입니다.
 </pre>