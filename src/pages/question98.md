- info
    - lv2
    - 백트래킹

# N-Queen 문제
## 문제 설명
N x N 크기의 체스판에 N개의 퀸을 서로 공격할 수 없도록 배치하는 문제입니다. 
퀸은 체스에서 가장 강력한 기물로, 가로, 세로, 대각선 방향으로 이동할 수 있습니다.
N이 주어졌을 때, 퀸을 배치하는 방법의 수를 구하는 프로그램을 작성해주세요.

---

## 제한 사항

- N은 1 이상 15 이하의 자연수입니다.
- 백트래킹 알고리즘을 이용하여 문제를 해결해야 합니다.

---

## 입출력 예

| 입력 | 출력 |
| ---- | ---- |
| 1    | 1    |
| 2    | 0    |
| 3    | 0    |
| 4    | 2    |
| 5    | 10   |
| 6    | 4    |
| 7    | 40   |
| 8    | 92   |

---

## 입출력 설명
- 첫 번째 예시에서 N이 1일 때, 퀸을 배치하는 방법은 1가지입니다.
- 두 번째 예시에서 N이 2일 때, 퀸을 서로 공격하지 않도록 배치하는 방법은 없습니다.
- 세 번째 예시에서 N이 3일 때, 퀸을 서로 공격하지 않도록 배치하는 방법은 없습니다.
- 네 번째 예시에서 N이 4일 때, 퀸을 서로 공격하지 않도록 배치하는 방법은 2가지입니다.
- 다섯 번째 예시에서 N이 5일 때, 퀸을 서로 공격하지 않도록 배치하는 방법은 10가지입니다.
- 여섯 번째 예시에서 N이 6일 때, 퀸을 서로 공격하지 않도록 배치하는 방법은 4가지입니다.
- 일곱 번째 예시에서 N이 7일 때, 퀸을 서로 공격하지 않도록 배치하는 방법은 40가지입니다.
- 여덟 번째 예시에서 N이 8일 때, 퀸을 서로 공격하지 않도록 배치하는 방법은 92가지입니다.