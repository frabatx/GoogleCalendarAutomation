from utils.get_service import get_calendar_service
from responses.response_json import response_json

service = get_calendar_service()

def create_event(template: dict):
    try:
        responce = service.events().insert(calendarId = 'primary', body=template).execute()
        return responce
    except Exception as e:
        return response_json(message=e.message, status = 500)


def get_event(eventId: str):
    try:
        responce = service.events().get(calendarId = 'primary', eventId=eventId).execute()
        return responce
    except Exception as e:
        return response_json(message=e.message, status = 500)

def delete_event(eventId: str):
    try:
        responce = service.events().delete(calendarId = 'primary', eventId=eventId).execute()
        return responce
    except Exception as e:
        return response_json(message=e.message, status = 500)

def update_event(eventId: str, template: dict):
    try:
        responce = service.events().update(calendarId = 'primary', eventId=eventId, body=template).execute()
        return responce
    except Exception as e:
        return response_json(message=e.message, status = 500)
