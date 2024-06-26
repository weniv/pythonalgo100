- info
    - lv1
    - 좌표평면

# 겹치는 선 길이 구하기
## 문제 설명
세 개의 선분의 시작점과 끝점이 주어집니다. 각 선분은 1차원 좌표상에서 시작점과 끝점으로 표현됩니다. 이 세 선분이 겹치는 부분의 길이를 구하는 코드를 작성해주세요. 만약 세 선분이 겹치지 않는다면, 0을 반환합니다.

---

## 제한 사항

- 선분의 시작점과 끝점은 정수로 주어집니다.
- 각 선분은 [시작점, 끝점]의 형태로 주어집니다.
- 좌표의 범위는 0 이상 100 이하입니다.
- 세 선분이 겹치는 경우만 고려합니다.

---

## 입출력 예

| 입력 (선분1, 선분2, 선분3) | 출력 (겹치는 길이) |
| -------------------------- | ------------------ |
| [1, 5], [3, 7], [2, 6] | 2 |
| [0, 1], [1, 6], [3, 4] | 0 |
| [10, 15], [12, 20], [14, 18] | 1 |

---

## 입출력 설명
세 선분이 겹치는 부분의 길이를 계산합니다. 예를 들어, 선분 [1, 5], [3, 7], [2, 6]의 겹치는 부분은 3부터 5까지이며, 그 길이는 2입니다.
