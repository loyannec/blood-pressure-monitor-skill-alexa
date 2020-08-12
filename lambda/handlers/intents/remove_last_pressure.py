# -*- coding: utf-8 -*-

from .base_intent_handler import BaseIntentHandler
from core import Pressure


class RemoveLastPressureIntentHandler(BaseIntentHandler):
    def __init__(self):
        super().__init__('RemoveLastPressureIntent')

    def handle(self, handler_input):
        speak_output = 'There is no blood pressure recorded yet.'

        # Deletes and updates the list of pressures only if at least one pressure was recorded before.
        if self.pressures_size():
            pressure = self.pop_last_pressure()
            speak_output = f'Your last pressure {pressure.systolic_number} by {pressure.diastolic_number} was removed.'
            self._log(f'current size: {self.pressures_size()}')

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
