from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict


class ResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class OrderConstraint(BaseModel):
    currency: str = Field(description='화폐를 의미하는 영문 대문자 코드')
    # price_unit: str = Field(description='주문금액 단위')
    min_total: int = Field(description='최소 매도/매수 금액')


class Bid(OrderConstraint):
    """ 매수시 제약사항 """
    pass


class Ask(OrderConstraint):
    """ 매도시 제약사항 """
    pass


class Market(BaseModel):
    id: str
    name: str
    order_sides: List[str] = Field(description='지원 주문 종류')
    max_total: int = Field(description='최대 매도/매수 금액')
    state: str = Field(description='마켓 운영 상태')
    ask_types: List[str] = Field(description='매도 주문 지원 방식')
    bid_types: List[str] = Field(description='매수 주문 지원 방식')
    bid: Bid = Field(description='매수 시 제약사항')
    ask: Ask = Field(description='매도 시 제약사항')


class OrderAccount(BaseModel):
    currency: str = Field(description='화폐를 의미하는 영문 대문자 코드')
    balance: float = Field(description='주문가능 금액/수량')
    locked: str = Field(description='주문 중 묶여있는 금액/수량')
    avg_buy_price: float = Field(description='매수평균가')
    avg_buy_price_modified: bool = Field(description='매수평균가 수정 여부')
    unit_currency: str = Field(description='평단가 기준 화폐')


class BidAccount(OrderAccount):
    pass


class AskAccount(OrderAccount):
    pass


class OrderChance(ResponseBase):
    bid_fee: float = Field(description='매수 수수료 비율')
    ask_fee: float = Field(description='매도 수수료 비율')
    maker_bid_fee: float
    maker_ask_fee: float
    market: Market = Field(description='코인 정보')
    bid_account: BidAccount
    ask_account: AskAccount


class OrderHistory(ResponseBase):
    uuid: str = Field(description='주문의 고유 아이디')
    side: str = Field(description='주문 종류')
    ord_type: str = Field(description='주문 방식')
    price: int = Field(description='주문 당시 화폐 가격', default=0)
    state: str = Field(description='주문 상태')
    market: str = Field(description='마켓의 유일키')
    created_at: str = Field(description='주문 생성 시간')
    volume: float = Field(description='사용자가 입력한 주문 양')
    remaining_volume: float = Field(description='체결 후 남은 주문 양')
    reserved_fee: float = Field(description='수수료로 예약된 비용')
    remaining_fee: float = Field(description='남은 수수료')
    paid_fee: float = Field(description='사용된 수수료')
    locked: float = Field(description='거래에 사용중인 비용')
    executed_volume: float = Field(description='체결된 양')
    trades_count: int = Field(description='해당 주문에 걸린 체결 수')
    """
    uuid	주문의 고유 아이디	String
    side	주문 종류	String
    ord_type	주문 방식	String
    price	주문 당시 화폐 가격	NumberString
    state	주문 상태	String
    market	마켓의 유일키	String
    created_at	주문 생성 시간	DateString
    volume	사용자가 입력한 주문 양	NumberString
    remaining_volume	체결 후 남은 주문 양	NumberString
    reserved_fee	수수료로 예약된 비용	NumberString
    remaining_fee	남은 수수료	NumberString
    paid_fee	사용된 수수료	NumberString
    locked	거래에 사용중인 비용	NumberString
    executed_volume	체결된 양	NumberString
    trades_count	해당 주문에 걸린 체결 수	Integer
    """
