#!/usr/bin/env python
from fastapi import FastAPI
from utils.get_service import get_calendar_service
from routes.calendar import routes_calendar

# app = create_app()
app = FastAPI()
app.include_router(routes_calendar)
get_calendar_service()


# if __name__ == '__main__':
    # uvicorn.run(app)
