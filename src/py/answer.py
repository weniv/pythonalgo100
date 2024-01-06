# 1
def solution(data):
    return sum(filter(lambda x: x % 2, data))


# 2
def solution(data):
    if not data:
        return 0
    result = 1
    for x in data:
        if x == 0:
            return 0
        result *= x
    return result


# 3
def solution(data):
    return sum(filter(lambda x: not (x % 3 == 0 or x % 5 == 0), data))


# 4
def solution(data):
    result = 0
    for i, s in enumerate(data):
        number = int(s.split(" ")[1].replace("개", ""))
        result += number * (i + 1)
    return result


# 5
def solution(data):
    return "".join(map(str, data)).count("1")


# 6
def solution(data):
    return sum(map(int, filter(str.isdigit, data)))


# 7
def solution(data):
    return list(map(lambda x: x[0], sorted(data, key=lambda x: x[1])))


# 8
def solution(data):
    return list(sorted(zip(data, data[1:]), key=lambda x: x[1] - x[0])[0])


# 9
def solution(data):
    return sorted(data, key=lambda x: x["수"], reverse=True)[0]["이름"]


# 10
def solution(data):
    return sorted(map(lambda x: x[0], filter(lambda x: sum(x[1:]) > 350, data)))


# 11
def solution(data):
    return len(list(filter(lambda x: sum(x) > 240, data)))


# 12
def solution(data):
    return sorted(data[0], key=lambda x: data[1].get(x.split(" ")[1]))


# 13
def solution(data):
    books, publish_years = data
    return sorted(books, key=lambda book: (publish_years[book], book))


# 14
def solution(data):
    sorted_data = sorted(data.keys())
    return [data[i] for i in sorted_data]


# 15
def solution(times):
    def convert_time(time):
        hh, mm, ampm = time.split(" ")[0].split(":") + time.split(" ")[1:]

        # 12시간제를 24시간제로 변환합니다. 12:00 AM은 00:00으로, 12:00 PM은 12:00으로 처리합니다.
        if ampm == "PM" and hh != "12":
            hh = str(int(hh) + 12)
        elif ampm == "AM" and hh == "12":
            hh = "00"

        return hh + ":" + mm + " " + ampm

    # 변환된 시간을 오름차순으로 정렬합니다.
    return sorted(times, key=convert_time)


# 16
def solution(dates):
    def convert_date(date):
        # 날짜 구분자에 따라 날짜를 분리합니다.
        if "-" in date:
            day, month, year = date.split("-")
        elif "/" in date:
            month, day, year = date.split("/")
        else:  # '.' 구분자
            year, month, day = date.split(".")

        return year, month, day

    # 날짜들을 연/월/일 형식으로 변환합니다.
    converted_dates = [convert_date(date) for date in dates]

    # 변환된 날짜들을 오름차순으로 정렬합니다.
    sorted_dates = sorted(converted_dates)

    # 정렬된 날짜들을 '연/월/일' 형식으로 다시 변환합니다.
    return ["/".join(date) for date in sorted_dates]


# 17
# 모듈 사용
from datetime import datetime


def solution(schedules):
    # 모든 일정을 하나의 리스트로 변환하면서 요일 정보를 함께 저장합니다.
    all_schedules = []
    for day, dates in schedules.items():
        for date in dates:
            all_schedules.append((date, day))

    # 날짜를 기준으로 내림차순 정렬합니다.
    all_schedules.sort(key=lambda x: x[0], reverse=True)

    # 최근 3개의 일정을 선택합니다.
    recent_three = all_schedules[:3]

    # 선택된 일정을 'YY-MM-DD 요일' 형식으로 변환합니다.
    return [
        datetime.strptime(date, "%Y-%m-%d").strftime("%y-%m-%d") + " " + day
        for date, day in recent_three
    ]


# test
from datetime import datetime

datetime.strptime("2024-01-01", "%Y-%m-%d").strftime("%y-%m-%d")


# 모듈 사용하지 않음
def solution(schedules):
    # 모든 일정을 하나의 리스트로 변환하면서 요일 정보를 함께 저장합니다.
    all_schedules = []
    for day, dates in schedules.items():
        for date in dates:
            # 날짜를 'YYYY-MM-DD'에서 'YY-MM-DD 요일' 형식으로 변환합니다.
            converted_date = date[2:] + " " + day
            all_schedules.append(converted_date)

    # 변환된 일정을 내림차순으로 정렬합니다.
    all_schedules.sort(reverse=True)

    # 최근 3개의 일정을 선택합니다.
    return all_schedules[:3]


def solution(data):
    all_schedules = []

    for day, dates in data.items():
        for date in dates:
            converted_date = f"{date[2:]} {day}"
            all_schedules.append(converted_date)
    all_schedules.sort(reverse=True)
    return all_schedules[:3]


# 18
def solution(temperature_data):
    # 온도 데이터를 (온도, 날짜) 형식의 튜플 리스트로 변환합니다.
    temp_list = [(temp, date) for date, temp in temperature_data.items()]

    # 온도를 기준으로 내림차순 정렬하되, 온도가 같은 경우 날짜를 기준으로 오름차순 정렬합니다.
    temp_list.sort(key=lambda x: (-x[0], x[1]))

    # 최고 온도 상위 3일을 선택합니다.
    top_three = temp_list[:3]

    # 선택된 날짜를 'YY-MM-DD: 온도' 형식으로 변환합니다.
    return [date[2:] + ": " + str(temp) for temp, date in top_three]


# 테스트
test_data = {
    "2024-01-01": 15,
    "2024-01-02": 17,
    "2024-01-03": 16,
    "2024-01-04": 20,
    "2024-01-05": 19,
    "2024-01-06": 21,
    "2024-01-07": 18,
}
print(solution(test_data))


def solution(data):
    temp_list = [(temp, date) for date, temp in data.items()]
    temp_list.sort(key=lambda x: (-x[0], x[1]))
    top_three = temp_list[:3]
    return [f"{date[2:]}: {temp}" for temp, date in top_three]


# 19
def solution(data_list):
    # 각 항목의 데이터 타입을 확인하고 타입 이름을 문자열로 반환합니다.
    return [type(item).__name__ for item in data_list]


# 테스트
test_data = [123, 4.56, "hello", [1, 2, 3], (4, 5), {"a": 1, "b": 2}]
print(solution(test_data))


# 20
def solution(class_instance_pairs):
    # 각 클래스와 인스턴스 쌍에 대해 isinstance 함수를 사용하여 타입 확인을 수행합니다.
    return all(
        [type(instance).__name__ == class_ for class_, instance in class_instance_pairs]
    )


# 테스트
test_pairs = [(list, [1, 2, 3]), (int, 4), (str, "hello")]
print(solution(test_pairs))


# 21
def solution(data):
    numbers, target = data
    # 주어진 배열에서 타겟 숫자의 위치를 찾습니다.
    return numbers.index(target) if target in numbers else False


# 테스트
test_data_1 = ([1, 3, 5, 7, 9], 5)
print(solution(test_data_1))

test_data_2 = ([2, 4, 6, 8, 10], 7)
print(solution(test_data_2))


# 22
def solution(data):
    s, target = data
    return s.find(target) if target in s else False


# 23
def solution(data):
    matrix, target = data
    # 각 행을 순회하며 타겟 숫자 탐색
    for row in matrix:
        if target in row:
            return True
    return False


def solution(data):
    matrix, target = data
    return any([target in row for row in matrix])


def solution(data):
    matrix, target = data
    return target in sum(matrix, [])


# 24
# 카데인 알고리즘
# 현재까지의 최대 합과 현재 위치에서의 최대합을 갱신합니다.
# 이 알고리즘은 현재 위치까지의 최대합이 음수인 경우 현재 위치부터 다시 더하기 시작하는 알고리즘입니다.
# 음수가 아니면 더해나가는 것이 최대합이 되는 것을 응용한 것입니다.
def solution(data):
    if not data:
        return 0

    max_sum = current_sum = data[0]

    for num in data[1:]:
        print(num)
        # 현재 값인 num과 현재 위치까지의 최대합과 num을 더한 값 중 큰 값을 현재 위치까지의 최대합으로 설정합니다. 이전까지 더한 값이 음수인 경우 '현재 값'부터 다시 더하기 시작합니다.
        current_sum = max(num, current_sum + num)
        # 이렇게 설정된 현재 위치까지의 최대합을 최대 합과 비교하여 더 큰 값을 최대 합으로 설정합니다.
        max_sum = max(max_sum, current_sum)
        print("-----------")

    return max_sum


# 25
def solution(N):
    prime = [True] * (N + 1)
    prime[0] = prime[1] = False
    p = 2

    while p * p <= N:
        if prime[p]:
            for i in range(p * p, N + 1, p):
                prime[i] = False
        p += 1

    return sum(prime)


# 26
def solution(data):
    nums, k = data
    # 윈도우의 초기 합계 계산
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # 슬라이딩 윈도우를 이용해 최대 합계 탐색
    for i in range(len(nums) - k):
        window_sum = window_sum - nums[i] + nums[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum
