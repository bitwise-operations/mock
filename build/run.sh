#!/bin/sh

alembic upgrade head &&
uvicorn main:app --workers 8 --host 0.0.0.0 --port 8000
