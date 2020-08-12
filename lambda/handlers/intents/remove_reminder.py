# -*- coding: utf-8 -*-
import requests

from .base_intent_handler import BaseIntentHandler
from core import Pressure, PressureStatus


class RemoveReminderIntentHandler(BaseIntentHandler):
    def __init__(self):
        super().__init__('RemoveReminderIntent')

    def handle(self, handler_input):
        reminder = self.reminder_at_time()
        if reminder is None:
            speak_output = 'Sorry, I couldn\'t find this reminder.'
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
            )

        system = self.handler_input.request_envelope.context.system
        headers = { 'Authorization': f'Bearer {system.api_access_token}' }
        endpoint = f'{system.api_endpoint}/v1/alerts/reminders/{reminder.identifier}'

        self._log(f'Remove reminder: {reminder}')

        response = requests.delete(endpoint, headers=headers)

        self._log(f'Status code: {response.status_code}')

        response_json = response.json()
        self._log(response_json)

        if response.status_code in range(200, 204):
            speak_output = 'Okay, reminder was removed.'
            self.remove_reminder_by_id(reminder.identifier)
        else:
            speak_output = 'Something went wrong, please try again.'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
