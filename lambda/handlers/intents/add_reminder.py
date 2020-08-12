# -*- coding: utf-8 -*-
import requests
import datetime

from .base_intent_handler import BaseIntentHandler
from core import Pressure, PressureStatus


class AddReminderIntentHandler(BaseIntentHandler):
    def __init__(self):
        super().__init__('AddReminderIntent')

    def handle(self, handler_input):
        system = self.handler_input.request_envelope.context.system
        time = self.slot('time')
        if time == 'EV':
            time = '18:00'
        elif time == 'NI':
            time = '20:00'
        elif time == 'MO':
            time = '06:00'
        elif time == 'AF':
            time = '14:00'
        hour = time.split(':')[0]
        minute = time.split(':')[1]
        json = {
            "requestTime" : datetime.datetime.now().isoformat(),
            "trigger": {
                "type" : "SCHEDULED_ABSOLUTE",
                "timeZoneId" : "Europe/Dublin",
                "recurrence" : {
                    "recurrenceRules" : [
                        f"FREQ=DAILY;BYHOUR={hour};BYMINUTE={minute};",
                    ]
                }
            },
            "alertInfo": {
                "spokenInfo": {
                    "content": [{
                        "locale": "en-US",
                        "text": "It's time to register your blood pressure.",
                        "ssml": "<speak> It's time to register your blood pressure.</speak>"
                    }]
                }
            },
            "pushNotification" : {
                "status" : "ENABLED"
            }
        }
        headers = { 'Authorization': f'Bearer {system.api_access_token}' }
        endpoint = f'{system.api_endpoint}/v1/alerts/reminders'

        self._log(f'Add reminder to: {hour}:{minute}')

        response = requests.post(endpoint, json=json, headers=headers)

        self._log(f'Status code: {response.status_code}')
        self._log(response.json())
        speak_output = 'Alright, I will remind you when the time comes.'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
