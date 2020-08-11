# -*- coding: utf-8 -*-

from .base_intent_handler import BaseIntentHandler
from core import Pressure


class EditLastPressureIntentHandler(BaseIntentHandler):
    def __init__(self):
        super().__init__('EditLastPressureIntent')

    def handle(self, handler_input):
        speak_output = 'You haven\'t registered a pressure recently.'
        systolic_number = self.systolic_number()
        diastolic_number = self.diastolic_number()

        # Edit last pressure only if at least one pressure was recorded before.
        if self.pressures_size():
            if systolic_number and diastolic_number:
                pressure = Pressure(systolic_number, diastolic_number)
                self.update_last_pressure(pressure)
                speak_output = f'Your last pressure was edited to {pressure.systolic_number} by {pressure.diastolic_number}.'
            else:
                speak_output = f'You haven\'t said the systolic number or diastolic number.'

        self._log(speak_output)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
