# -*- coding: utf-8 -*-
from .base_intent_handler import BaseIntentHandler
from core import Pressure, PressureStatus


class RemoveRemindersIntentHandler(BaseIntentHandler):
    def __init__(self):
        super().__init__('RemoveRemindersIntent')

    def handle(self, handler_input):
        speak_output = 'Ready to go'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
