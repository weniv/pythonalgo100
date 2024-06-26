- info
    - lv0
    - 정렬

# 주간 최고 온도 기록 분석
## 문제 설명
일주일 동안의 최고 기온이 기록된 데이터가 주어집니다. 이 데이터에서 가장 높은 온도를 기록한 상위 3일을 찾아 'YY-MM-DD: 온도' 형식으로 반환하는 코드를 작성해주세요. 데이터는 'YYYY-MM-DD' 형식의 날짜와 해당 날짜의 최고 온도(섭씨)로 구성됩니다.

---

## 제한 사항

- 각 날짜의 최고 온도는 정수로 주어집니다.
- 기온 데이터는 최소 7개(일주일)에서 최대 30개(한달)까지 주어질 수 있습니다.
- 날짜는 중복되지 않습니다.
- 중복된 온도일 경우 날짜가 빠른 것이 앞에 정렬되어야 합니다.

---

## 입출력 예

|   입력 (기온 데이터)   | 출력 (상위 3일의 기온) |
| --------------------- | --------------------- |
| {'2024-01-01': 15, '2024-01-02': 17, '2024-01-03': 16, '2024-01-04': 20, '2024-01-05': 19, '2024-01-06': 21, '2024-01-07': 18} | ['24-01-06: 21', '24-01-04: 20', '24-01-05: 19'] |

---

## 입출력 설명
주어진 일주일 동안의 최고 기온 데이터에서 가장 높은 온도를 기록한 상위 3일을 'YY-MM-DD: 온도' 형식으로 반환합니다. 예를 들어, 가장 높은 기온을 기록한 날은 '2024-01-06'로 21도였으며, 그 다음은 '2024-01-04'의 20도, '2024-01-05'의 19도입니다.
