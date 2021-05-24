# BOJ-practice
백준 문제들을 가끔 풀어봅니다. 오늘부터는 진짜 하루에 하나씩 풀테야..

## 풀다가 집어치운 문제
* 2534: 카드 배열

## 해결된 문제
* 1149: RGB거리 (21/05/04)
* 1150: 백업
* 1629: 곱셈 (21/05/16)<br/>
  -내장 ```pow```함수에 이 기능이 있는지 처음 알았다.
* 1753: 최단경로 (21/05/07)<br/>
  -다익스트라에서 최솟값이 갱신될 때만 큐에 추가하는거랑 ```heapq```를 사용하여야 빠름을 깨달았다.
* 1865: 웜홀 (21/05/24)
* 1918: 후위 표기식 (21/05/21)<br/>
  -풀긴 풀었는데 머릿속에 있는걸 코드로 옮기는게 너무 어려웠다. 
* 1932: 정수삼각형 (21/05/05)
* 1991: 트리 순회 (21/05/09)
* 2206: 벽 부수고 이동하기 (21/05/14)<br/>
  -```collections.deque```의 존재를 깨달았다.  
* 2407: 조합 (21/05/19)
* 9251: LCS (21/05/11)
* 9465: 스티커 (21/05/08)
* 9663:  N-Queen (21/05/02)
* 11047: 동전0
* 11053: 가장 긴 증가하는 부분 수열 (21/05/06)
* 11054: 가장 긴 바이토닉 부분 수열 (21/05/13)
* 11404: 플로이드 (21/05/17)
* 11660: 구간 합 구하기 5 (21/05/20)
* 11719: 그대로 출력하기
* 11725: 트리의 부모 찾기 (21/05/18)</br>
  -그냥 큐가 쓰고싶어서 ```queue.Queue```를 썼는데 TLE로 머리를 싸맸다.
  ```deque```를 써서 결국 통과했다. 아마 ```queue.Queue```는 이럴 때 쓰는
  일반 큐가 아니고 멀티쓰레딩?과 관련해서 사용되는 조금 다른 기능인 것 같다.
* 12865: 평범한 배낭 (21/05/15)</br>
  -풀고나서 다른 사람들 풀이를 보았는데 2차원이 아닌 1차원 배열을 사용한 풀이가 인상적이었다.
* 13549: 숨바꼭질 3 (21/05/24)</br>
  -초기 위치가 0인 경우의 반례를 놓쳐서 고생했다.
* 14502: 연구소 (21/05/07) <br/>
  -별로 재미없는 Brute force
* 15591: MooTube (21/05/01)
* 15650: N과 M(2) (21/05/03) <br/>
  -```itertools```의 존재를 깨달았다.
* 15652: N과 M(4) (21/05/10)
* 15654: N과 M(5) (21/05/23)
* 15686: 치킨 배달 (21/05/12)
