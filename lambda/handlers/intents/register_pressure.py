# -*- coding: utf-8 -*-

import datetime
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.dispatch_components import AbstractRequestHandler

from .base_intent_handler import BaseIntentHandler
from core import Pressure


class RegisterPressureIntentHandler(BaseIntentHandler):
    def __init__(self):
        super().__init__('RegisterPressureIntent')

    def handle(self, handler_input):
        pressure = Pressure(self.systolic_number(), self.diastolic_number())
        self.add_pressure(pressure)
        self.set_can_edit_last_pressure(True)
        speak_output = f'Your pressure {pressure.systolic_number} by {pressure.diastolic_number} is normal.'

        print(f'RegisterPressureIntent: {speak_output}\n')

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
