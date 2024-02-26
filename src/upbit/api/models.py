from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, validator, field_validator


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


class Candle(ModelBase):
    market: str = Field(description='코인명')
    candle_date_time_utc: str = Field(description='utc 기준 시각')
    candle_date_time_kst: str = Field(description='kst 기준 시각')
    opening_price: float = Field(description='시가')
    high_price: float = Field(description='고가')
    low_price: float = Field(description='저가')
    trade_price: float = Field(description='종가')
    timestamp: float = Field(description='마지막 틱이 저장된 시각')
    candle_acc_trade_price: float = Field(description='누적 거래 금액')
    candle_acc_trade_volume: float = Field(description='누적 거래량')

    @field_validator('candle_date_time_kst')
    @classmethod
    def _convert_date_format(cls, v: str) -> str:
        """
        문자열 날짜 형식 변경
        예시)
            이전 : 2024-02-16T00:00:00
            변경 : 2024-02-16

        :param v: 2024-02-16T00:00:00
        :return: 2024-02-16
        """
        return str(datetime.strptime(v, "%Y-%m-%dT%H:%M:%S").date())


class DayCandle(Candle):
    prev_closing_price: float = Field(description='전일 종가(utc 0시 기준)')
    change_price: Optional[float] = Field(description='전일 종가 대비 변화 금액', default=None)
    change_rate: float = Field(description='전일 종가 대비 변화량')
    converted_trade_price: Optional[float] = Field(description='종가 환상 화폐 단위로 환산된 가격', default=None)