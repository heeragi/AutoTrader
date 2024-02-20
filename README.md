# AutoTrader

# 업비트 자동 매매 프로그램

## 사용법

1. api key 발급 (업비트 로그인 필요) [업비트 API KEY 발급 링크](https://upbit.com/mypage/open_api_management)
2. python package 설치
    
    ```bash
    pip install poetry
    poetry install
    poetry shell
    ```
    


## 개발자 문서
[업비트 개발자 문서 링크](https://docs.upbit.com/reference/전체-계좌-조회)


## 프로젝트 구조

main.py - 프로젝트 시작점

src - 소스 폴더

src > upbit > api - 업비트 api 모듈

tests - 유닛 테스트