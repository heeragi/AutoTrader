from pydantic import BaseModel, ConfigDict, Field


class ModelBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class Account(BaseModel):
    currency: str = Field(description='화폐를 의미하는 영문 대문자 코드')
    balance: float = Field(description='주문가능 금액 및 수량')
    locked: float = Field(description='주문 중 묶여있는 금액 및 수량')
    avg_buy_price: float = Field(description='매수 평균가')
    avg_buy_price_modified: bool = Field(description='매수 평균가 수정 여부')
    unit_currency: str = Field(description='평단가 기준 화폐')


class Coin(BaseModel):
    market: str
    korean_name: str
    english_name: str
    market_warning: str