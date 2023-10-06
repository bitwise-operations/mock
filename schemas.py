from pydantic import BaseModel
from typing import Optional


class EventAppFlyer(BaseModel):
    idfa: Optional[str] = None
    idfv: Optional[str] = None
    appsflyer_id: Optional[str] = None
    customer_user_id: Optional[str] = None
    att: Optional[int] = None
    eventName: Optional[str] = None
    eventValue: Optional[str] = None
    eventTime: Optional[str] = None
    eventCurrency: Optional[str] = None
    bundleIdentifier: Optional[str] = None
    os: Optional[str] = None
    advertising_id: Optional[str] = None
    aie: Optional[str] = None


class ResponseEvent(EventAppFlyer):
    id: int


class GrpcRequest(BaseModel):
    endpoint: Optional[str] = None
    service: Optional[str] = None
    method: Optional[str] = None
    request_json: Optional[dict] = None
    ssl: Optional[bool] = None
