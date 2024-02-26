from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class UpbitAPIRequestBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class DayCandleRequest(UpbitAPIRequestBase):
    market: str = Field(description='마켓코드', default='KRW-BTC')
    to: Optional[str] = Field(description='마지막 캔들 시각', default=None)
    count: int = Field(description='마켓코드', default=200)
    convertingPriceUnit: str = Field(description='마켓코드', default='KRW')
