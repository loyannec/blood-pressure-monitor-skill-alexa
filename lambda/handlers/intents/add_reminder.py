# -*- coding: utf-8 -*-
import requests
import datetime

from .base_intent_handler import BaseIntentHandler
from core import Pressure, PressureStatus, Reminder


class AddReminderIntentHandler(BaseIntentHandler):
    def __init__(self):
        super().__init__('AddReminderIntent')

    def handle(self, handler_input):
        if self.reminder_at_time() is not None:
            speak_output = 'Okay, this reminder is already set.'
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
            )

        system = self.handler_input.request_envelope.context.system
        hour = self.hour()
        minute = self.minute()
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

        response_json = response.json()
        self._log(response_json)

        if 'alertToken' in response_json:
            speak_output = 'Alright, I will remind you when the time comes.'
            self.add_reminder(Reminder(identifier=response_json['alertToken'], hour=hour, minute=minute))
        else:
            speak_output = 'Something went wrong, please try again.'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
