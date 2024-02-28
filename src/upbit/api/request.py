from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict


class UpbitAPIRequestBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class DayCandleRequest(UpbitAPIRequestBase):
    market: str = Field(description='마켓코드', default='KRW-BTC')
    to: Optional[str] = Field(description='마지막 캔들 시각', default=None)
    count: int = Field(description='가져올 캔들 개수', default=200)
    convertingPriceUnit: str = Field(description='마켓코드', default=None)

class MinuteCandleRequest(UpbitAPIRequestBase):
    market: str = Field(description='마켓코드', default='KRW-BTC')
    to: Optional[str] = Field(description='마지막 캔들 시각', default=None)
    count: int = Field(description='캔들 개수', default=200)

class WeekCandleRequest(UpbitAPIRequestBase):
    market: str = Field(description='마켓코드', default='KRW-BTC')
    to: Optional[str] = Field(description='마지막 캔들 시각', default=None)
    count: int = Field(description='캔들 개수', default=200)

class MonthCandleRequest(UpbitAPIRequestBase):
    market: str = Field(description='마켓코드', default='KRW-BTC')
    to: Optional[str] = Field(description='마지막 캔들 시각', default=None)
    count: int = Field(description='캔들 개수', default=200)


class OrderListRequest(UpbitAPIRequestBase):
    market: str = Field(description='마켓 아이디', default='KRW-BTC')
    uuids: Optional[List[str]] = Field(description='주문 UUID의 목록', default=[])
    identifiers: Optional[List[str]] = Field(description='주문 identifier의 목록', default=[])
    state: str = Field(description='''주문 상태
        - wait : 체결 대기 (default)
        - watch : 예약주문 대기
        - done : 전체 체결 완료
        - cancel : 주문 취소
        
        - 주문 리스트 조회 API에서 시장가 주문이 조회되지 않는경우: 시장가 매수 주문은 체결 후 주문 상태가 cancel, done 두 경우 모두 발생할 수 있습니다.
        - 시장가로 체결이 일어난 후 주문 잔량이 발생하는 경우, 남은 잔량이 반환되며 cancel 처리됩니다. 대부분의 경우 소수점 아래 8자리까지 나누어 떨어지지 않는 미미한 금액이 주문 잔량으로 발생하게 됩니다.
        - 만일 주문 잔량 없이 딱 맞아떨어지게 체결이 발생한 경우에는 주문 상태가 done이 됩니다.
    ''', default='done')
    states: Optional[List[str]] = Field(description='''주문 상태의 목록
        * 미체결 주문(wait, watch)과 완료 주문(done, cancel)은 혼합하여 조회하실 수 없습니다.
    ''', default=[])
    page: int = Field(description='페이지 수', default=1)
    limit: int = Field(description='요청 개수', default=100)
    order_by: str = Field(description='정렬 방식', examples=['asc', 'desc'], default='desc')

class PostOrderRequest(UpbitAPIRequestBase):
    """
    market *	마켓 ID (필수)	String
    side *	주문 종류 (필수)
    - bid : 매수
    - ask : 매도	String
    volume *	주문량 (지정가, 시장가 매도 시 필수)	NumberString
    price *	주문 가격. (지정가, 시장가 매수 시 필수)
    ex) KRW-BTC 마켓에서 1BTC당 1,000 KRW로 거래할 경우, 값은 1000 이 된다.
    ex) KRW-BTC 마켓에서 1BTC당 매도 1호가가 500 KRW 인 경우, 시장가 매수 시 값을 1000으로 세팅하면 2BTC가 매수된다.
    (수수료가 존재하거나 매도 1호가의 수량에 따라 상이할 수 있음)	NumberString
    ord_type *	주문 타입 (필수)
    - limit : 지정가 주문
    - price : 시장가 주문(매수)
    - market : 시장가 주문(매도)	String
    identifier	조회용 사용자 지정값 (선택)	String (Uniq 값 사용)
    """
    market: str = Field(description='마켓 ID (필수)', default='KRW-BTC')
    side: str = Field(description='주문 종류 (필수)', examples=['bid', 'ask'], default='ask')
    volume: float = Field(description='주문량 (지정가, 시장가 매도 시 필수)', default=0)
    price: float = Field(description='주문 가격. (지정가, 시장가 매수 시 필수)', default=0)
    ord_type: str = Field(description='주문 타입 (필수)', examples=['limit', 'price', 'market'], default='limit')
    identifier: Optional[str] = Field(description='조회용 사용자 지정값 (선택)', default=None)
