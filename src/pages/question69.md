- info
    - lv1
    - 순열과 조합, 배열

# 특정 숫자 조합 찾기
## 문제 설명
정수 배열과 타겟 숫자가 주어집니다. 배열 내에서 선택할 수 있는 두 개의 숫자를 조합하여, 이들의 합이 주어진 타겟 숫자와 일치하는 모든 조합을 찾아 반환하는 코드를 작성해주세요. 반환되는 조합은 중복되지 않아야 하며, 각 조합은 오름차순으로 정렬되어야 합니다.

---

## 제한 사항

- 배열의 요소는 정수입니다.
- 배열의 길이는 1 이상 100 이하입니다.
- 각 요소의 값은 1 이상 100 이하입니다.
- 타겟 숫자는 1 이상 200 이하의 정수입니다.

---

## 입출력 예

| 입력 (정수 배열, 타겟 숫자) | 출력 (타겟 숫자를 만드는 숫자 조합) |
| --------------------------- | ----------------------------------- |
| ([1, 2, 3, 4, 5], 5) | [(1, 4), (2, 3)] |
| ([10, 20, 10, 40, 50, 60, 70], 50) | [(10, 40), (20, 30)] |
| ([5, 5, 10, 15, 20, 25], 30) | [(5, 25), (10, 20)] |

---

## 입출력 설명
주어진 배열에서 두 숫자를 선택하여 그 합이 타겟 숫자와 일치하는 모든 조합을 찾아 반환합니다. 예를 들어, 배열 [1, 2, 3, 4, 5]에서 합이 5가 되는 조합은 (1, 4)와 (2, 3)입니다.