- info
    - lv0
    - 탐색

# 2차원 배열 탐색
## 문제 설명
2차원 배열과 타겟 숫자가 주어집니다. 주어진 2차원 배열에서 타겟 숫자가 존재하는지 확인하고, 존재하는 경우 True를, 존재하지 않는 경우 False를 반환하는 코드를 작성해주세요.

---

## 제한 사항

- 2차원 배열은 m x n 크기이며, 각 요소는 정수입니다.
- 배열의 각 행은 오름차순으로 정렬되어 있습니다.
- m과 n은 각각 최소 1에서 최대 100까지입니다.

---

## 입출력 예

|   입력 (2차원 배열, 타겟 숫자)   | 출력 (숫자 존재 여부) |
| ------------------------------- | -------------------- |
| ([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 7) | True               |
| ([[2, 4, 6], [8, 10, 12], [14, 16, 18]], 13) | False              |

---

## 입출력 설명
주어진 2차원 배열에서 타겟 숫자를 찾아, 존재하는 경우 True를, 존재하지 않는 경우 False를 반환합니다. 첫 번째 예시에서는 타겟 숫자 7이 배열에 존재하므로 True를, 두 번째 예시에서는 타겟 숫자 13이 배열에 존재하지 않으므로 False를 반환합니다.
