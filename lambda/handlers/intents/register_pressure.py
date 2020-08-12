# -*- coding: utf-8 -*-

from .base_intent_handler import BaseIntentHandler
from core import Pressure, PressureStatus


class RegisterPressureIntentHandler(BaseIntentHandler):
    def __init__(self):
        super().__init__('RegisterPressureIntent')

    def handle(self, handler_input):
        pressure = Pressure(self.systolic_number(), self.diastolic_number())
        self.add_pressure(pressure)
        self.set_can_edit_last_pressure(True)
        speak_output = f'Your pressure {pressure.systolic_number} by {pressure.diastolic_number} is described as {pressure.status().description()}.'
        if pressure.status().value < 0:
            speak_output += ' If you are not feeling well call your GP.'
        self._log(speak_output)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
