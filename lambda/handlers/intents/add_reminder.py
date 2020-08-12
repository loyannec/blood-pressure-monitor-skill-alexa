# -*- coding: utf-8 -*-
import requests
import datetime

from .base_intent_handler import BaseIntentHandler
from core import Pressure, PressureStatus


class AddReminderIntentHandler(BaseIntentHandler):
    def __init__(self):
        super().__init__('AddReminderIntent')

    def handle(self, handler_input):
        system = self.handler_input.request_envelope.system
        json = {
            "requestTime" : datetime.datetime.now().isoformat(),
            "trigger": {
                "type" : "SCHEDULED_RELATIVE",
                "offsetInSeconds" : "10"
            },
            "alertInfo": {
                "spokenInfo": {
                    "content": [{
                        "locale": "en-US",
                        "text": "walk the dog",
                        "ssml": "<speak> walk the dog</speak>"
                    }]
                }
            },
            "pushNotification" : {
                "status" : "ENABLED"
            }
        }
        headers = { 'Authorization': system.api_access_token }
        endpoint = f'{system.api_endpoint}/v1/alerts/reminders'

        response = requests.post(endpoint, json=json, headers=headers)

        self._log(f'Status code: {response.status_code}')
        self._log(response.json())
        speak_output = 'Ready to go'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
