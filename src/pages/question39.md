- info
    - lv0
    - 정규표현식

# 파일 확장자 추출
## 문제 설명
주어진 파일 경로 또는 URL에서 파일 확장자를 추출하는 함수를 작성해주세요. 파일 확장자는 파일명 뒤에 오는 마지막 점(`.`) 뒤의 문자열입니다. 파일 확장자가 없는 경우, 빈 문자열을 반환합니다.

예를 들어, 문자열 "example/document.pdf"에서 함수는 `pdf`를, "example/folder"에서는 빈 문자열을 반환해야 합니다.

---

## 제한 사항

- 파일 경로 또는 URL은 문자열로 주어집니다.
- 파일 경로 또는 URL의 길이는 최대 1000자입니다.

---

## 입출력 예

|   입력 (파일 경로 또는 URL)     | 출력 (파일 확장자) |
| ----------------------------- | ------------------ |
| "example/document.pdf"        | "pdf"              |
| "https://www.example.com/image.jpg" | "jpg"              |
| "example/folder"              | ""                 |
| "archive.tar.gz"              | "gz"               |

---

## 입출력 설명
주어진 파일 경로 또는 URL에서 파일 확장자를 추출하여 반환합니다. 파일 확장자가 없는 경우 빈 문자열을 반환합니다.
