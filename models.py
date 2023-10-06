from sqlalchemy import Column, Integer, String
from database import Base


class EventAppFlyer(Base):
    __tablename__ = 'event_appflyer'

    id = Column(Integer, primary_key=True, nullable=False)
    app_id = Column(String(256), nullable=True, default=None)
    idfa = Column(String(256), nullable=True, default=None)
    idfv = Column(String(256), nullable=True, default=None)
    appsflyer_id = Column(String(256), nullable=True, default=None)
    customer_user_id = Column(String(256), nullable=True, default=None)
    att = Column(Integer, nullable=True, default=None)
    eventName = Column(String(256), nullable=True, default=None)
    eventValue = Column(String(256), nullable=True, default=None)
    eventTime = Column(String(256), nullable=True, default=None)
    eventCurrency = Column(String(256), nullable=True, default=None)
    bundleIdentifier = Column(String(256), nullable=True, default=None)
    os = Column(String(256), nullable=True, default=None)
    advertising_id = Column(String(256), nullable=True, default=None)
    aie = Column(String(256), nullable=True, default=None)
