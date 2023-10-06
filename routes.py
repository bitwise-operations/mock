from fastapi import APIRouter, HTTPException, Depends
import schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models


models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    with SessionLocal() as session:
        try:
            yield session
        except Exception:
            print("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()


def get_event(db: Session, appsflyer_id: str):
    event_app_flyer = db.query(
        models.EventAppFlyer).filter(
            models.EventAppFlyer.appsflyer_id == appsflyer_id).order_by(
                models.EventAppFlyer.id.desc()).first()
    return event_app_flyer


def create_event(db: Session, app_id: str, event: schemas.EventAppFlyer):
    event_app_flyer = models.EventAppFlyer(**event.dict(), app_id=app_id)
    db.add(event_app_flyer)
    db.commit()
    db.refresh(event_app_flyer)
    return event_app_flyer.__dict__


@router.get("/inappevent/{appsflyer_id}", response_model=schemas.ResponseEvent)
async def read_event(appsflyer_id: str, db: Session = Depends(get_db)):
    db_event = get_event(db=db, appsflyer_id=appsflyer_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event.__dict__


@router.post("/inappevent/{app_id}", response_model=schemas.ResponseEvent)
async def add_event(app_id: str, event: schemas.EventAppFlyer, db: Session = Depends(get_db)):
    return create_event(db=db, app_id=app_id, event=event)

