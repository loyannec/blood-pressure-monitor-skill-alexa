# -*- coding: utf-8 -*-
import requests

from .base_intent_handler import BaseIntentHandler
from core import Pressure, PressureStatus


class AddReminderIntentHandler(BaseIntentHandler):
    def __init__(self):
        super().__init__('AddReminderIntent')

    def handle(self, handler_input):
        json = {
            "requestTime" : "2019-09-22T19:04:00.672",
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

        response = requests.post('https://httpbin.org/post', json=json)
        self._log(f'Status code: {response.status_code}')
        self._log(response.json())
        speak_output = 'Ready to go'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
